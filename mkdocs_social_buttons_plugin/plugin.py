from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config import config_options

from .utils import button_name_to_class, strip_seps_fn

import pkgutil

from . import buttons

import logging

logger = logging.getLogger("mkdocs.plugins")

# Populate a dictionary of { button_name: button_class } based on the
def button_class(name):
    return getattr(getattr(buttons, name), button_name_to_class(name))
buttons_class_dict = { b.name: button_class(b.name) for b in pkgutil.iter_modules(buttons.__path__) if b.name != "base" }

class ButtonConfig(Config):
    ''' Config for a button definition '''
    message = config_options.Optional(config_options.Type(str))

def populate_button_config(cls):
    # Decorator to load the config structure for each implemented button type
    for b in buttons_class_dict.keys():
        logger.info(f"social-buttons: found {b} button module")
        option_item = config_options.SubConfig(ButtonConfig)
        setattr(cls, b, option_item)

        # Unfortunate hack to get around MKDocs initialising the schema so early
        cls._schema = cls._schema + ((b, option_item),)

    return cls

@populate_button_config
class PluginConfig(Config):
    ''' Config for Social Buttons Plugin '''
    # Note buttons are populated dynamically by the decorator.

    # Default settings
    default_message = config_options.Type(str, default="This was shared using the MKDocs Social Buttons plugin!")
    alternative_url_root = config_options.Optional(config_options.Type(str))
    apply_to_paths = config_options.ListOfItems(config_options.Type(str), default=[])
    exclude_hashtags = config_options.ListOfItems(config_options.Type(str), default=[])
    button_style = config_options.Type(str, default="")
    button_class = config_options.Type(str, default="")


class SocialButtonsPlugin(BasePlugin[PluginConfig]):
    ''' Main class for Social Buttons Plugin '''

    def on_config(self, config):
        # Use this function to generate all the button objects from the known supported buttons
        self.buttons = {name: cls(self.config) for name, cls in buttons_class_dict.items()}

    # Handle the on_page_context event
    def on_page_context(self, context, page, config, nav):
        # Inject social buttons into the context
        if self.config.apply_to_paths and not any(map(page.url.startswith, self.config.apply_to_paths)):
            logger.info(f'social-buttons: skipping path: /{page.url}')
            return context

        logger.debug(f'Handle page context for {page.title}')

        # Get any tags defined in the page
        tags = list(
                filter(lambda x: x not in self.config.exclude_hashtags,
                    map(str.lower, map(strip_seps_fn(), page.meta.get('tags', [])))
                    )
                )

        # Apply additional configuration
        page_url = page.canonical_url
        if self.config['alternative_url_root']:
            page_url = self.config['alternative_url_root'] + page.abs_url

        # call the correct button class method for each defined class
        def style_button(item):
            return f'<li class="{self.config.button_class}" style="{self.config.button_style}">{item}</li>'
        button_list = ''.join(map(style_button, (b.generate(page_url, hashtags=tags) for b in self.buttons.values())))
        script_list = ''.join(b.get_script() for b in self.buttons.values())

        # Update context
        context['social_buttons'] = button_list
        context['social_buttons_scripts'] = script_list

        return context
