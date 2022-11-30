from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config import config_options

import pkgutil
import re
from functools import partial

from . import buttons

import logging

logger = logging.getLogger("mkdocs.plugins")

### Helper functions
# Replace unsupported characters in a string
strip_chars = partial(re.sub, r'/[ \-]/', '')

# Populate a dictionary of { button_name: button_class } based on the
def button_class(x):
    return getattr(getattr(buttons, x), x.capitalize() + "Button")
buttons_class_dict = { b.name: button_class(b.name) for b in pkgutil.iter_modules(buttons.__path__) if b.name != "base" }
logger.info(buttons_class_dict)

class ButtonConfig(Config):
    ''' Config for a button definition '''
    message = config_options.Optional(config_options.Type(str,default=None))

def populate_button_config(cls):
    # Decorator to load the config structure for each known button type
    for b in buttons_class_dict.keys():
        logger.info(f"social-buttons: found {b} button module")
        setattr(cls, b, config_options.SubConfig(ButtonConfig))

    return cls

@populate_button_config
class PluginConfig(Config):
    ''' Config for Social Buttons Plugin '''
    # Supported Buttons from buttons folder
    linkedin = config_options.SubConfig(ButtonConfig)

    # Default settings
    default_message = config_options.Type(str, default="This was shared using the MKDocs Social Buttons plugin!")


class SocialButtonsPlugin(BasePlugin[PluginConfig]):
    ''' Main class for Social Buttons Plugin '''

    def on_config(self, config):
        # Use this function to generate all the button objects from the known supported buttons
        self.buttons = {name: cls(self.config) for name, cls in buttons_class_dict.items()}

    # Handle the on_page_context event
    def on_page_context(self, context, page, config, nav):
        # Inject social buttons into the context
        logger.debug(f'Handle page context for {page.title}')
        tags = list(map(strip_chars, page.meta.get('tags', [])))

        # call the correct button class method for each defined class
        button_list = ''.join(b.generate(page.canonical_url, tags) for b in self.buttons.values())
        script_list = ''.join(b.get_script() for b in self.buttons.values())

        context['social_buttons'] = button_list
        context['social_buttons_scripts'] = script_list

        return context
