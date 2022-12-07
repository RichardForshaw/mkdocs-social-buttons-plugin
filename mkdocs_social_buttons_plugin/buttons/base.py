import inspect

import logging

logger = logging.getLogger("mkdocs.plugins")

def tuple_to_html_attr(t):
    ''' Convert ("attr_foo", "bar") into data-foo="bar" '''
    return f'{t[0].replace("_", "-").replace("attr", "data")}="{t[1]}"'

class ButtonBase():
    ''' Base class for generating social buttons. Handles MKDocs config details. '''
    # Data defaults
    config_name = None
    button_text = ''
    button_style = ''

    # Script text
    button_script = None
    handler_script = None
    handler_callback = None

    def __init__(self, config):
        ''' Create object, handle MKDocs config '''
        # Error checking
        if not self.config_name:
            raise NotImplementedError("Missing required attribute: config_name")
        if not self.button_script:
            raise NotImplementedError("Missing required attribute: button_script")

        button_config = config.get(self.config_name, {})
        logger.debug(f"Building {self.config_name} button with config: {button_config}")

        # Get the correct sharing text
        FALLBACK_MESSAGE = 'Shared from MKDocs'
        self.share_message = button_config.get('message', None) or config.get('default_message', FALLBACK_MESSAGE)

        # Store handler callback if it exists
        self.handler_callback = button_config.get('button_share_callback', None)

    def generate(self, share_url, **kwargs):
        ''' Generate HTML based on the declared sub-class values'''
        logger.debug(f"Generating {self.config_name} button for {share_url}")
        # Helper lambdas
        attr_filter = lambda x: x[0].startswith('attr_')
        is_string = lambda x: isinstance(x, str)

        # Get extra attributes from the class definition
        additional_attrs = ' '.join(map(tuple_to_html_attr, filter(attr_filter, inspect.getmembers(self, is_string))))

        return self.render_html(share_url, additional_attrs)

    def render_html(self, share_url, additional_attrs):
        # Pure function - required to be implemented in child class.
        raise NotImplementedError

    def get_script(self, mkd_page={}):
        ''' Get the script needed for the buttons to work '''
        if self.handler_script and self.handler_callback:
            # If the user has provided a callback, and there is a script configured to support it
            return self.button_script + self.handler_script.format(handler=self.handler_callback, page=mkd_page)

        return self.button_script

class LinkButton(ButtonBase):
    ''' A type of button which generates a href-type link '''
    # Specific properties
    button_url = None

    def __init__(self, config):
        # Error checking. This button type requires a url to be defined
        if not self.button_url:
            raise NotImplementedError("Missing required attribute: button_url")

        super(LinkButton, self).__init__(config)

    def render_html(self, share_url, additional_attrs):
        # Render the components into a string
        return f'<a href="{self.button_url}" {self.button_style} data-text="{self.share_message}" data-url="{share_url}" {additional_attrs}>{self.button_text}</a>'

class ScriptButton(ButtonBase):
    ''' A type of button which generates a script tag '''
    # Specific properties
    script_type = None

    def __init__(self, config):
        # Error checking. This button type requires a url to be defined
        if not self.script_type:
            raise NotImplementedError("Missing required attribute: button_url")

        super(ScriptButton, self).__init__(config)

    def render_html(self, share_url, additional_attrs):
        # Render the components into a string
        return f'<script type="{self.script_type}" data-url="{share_url}">{self.button_text}</script>'

