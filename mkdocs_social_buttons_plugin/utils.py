# Utilities for the plugin

import re
from functools import partial

def strip_space_fn(rep=''):
    # Replace spaces in a string
    return partial(re.sub, ' ', rep)

def strip_seps_fn(rep=''):
    # Replace spaces, hyphens and underscores in a string
    return partial(re.sub, r'[ _\-]', rep)

def button_name_to_class(name):
    print(strip_seps_fn(' ')(name).capitalize())
    return strip_space_fn()(strip_seps_fn(' ')(name).title()) + "Button"
