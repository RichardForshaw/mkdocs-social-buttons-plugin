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
    button_url = None
    button_text = ''
    button_style = ''
    button_script = ''

    def __init__(self, config):
        ''' Create object, handle MKDocs config '''
        # Error checking
        if not self.config_name:
            raise NotImplementedError("Missing required attribute: config_name")
        if not self.button_url:
            raise NotImplementedError("Missing required attribute: button_url")

        logger.info(f"Building {self.config_name} button with config: {config}")
        if self.config_name in config:
            self.share_message = config[self.config_name]['message']
        else:
            self.share_message = config.get('default_message', 'Shared from MKDocs')

    def generate(self, share_url):
        ''' Generate HTML based on the declared sub-class values'''
        logger.debug(f"Generating {self.config_name} button for {share_url}")
        # Helper lambdas
        attr_filter = lambda x: x[0].startswith('attr_')
        is_string = lambda x: isinstance(x, str)

        # Get extra attributes from the class definition
        additional_attrs = ' '.join(map(tuple_to_html_attr, filter(attr_filter, inspect.getmembers(self, is_string))))

        return f'<a href="{self.button_url}" {self.button_style} data-text="{self.share_message}" data-url="{share_url}" {additional_attrs}>{self.button_text}</a>'

    def get_script(self):
        ''' Get the script needed for the buttons to work '''
        return self.button_script
