# Utilities for the plugin

import re
from functools import partial

def strip_space_fn(rep=''):
    # Replace spaces in a string
    return partial(re.sub, ' ', rep)

def strip_seps_fn(rep=''):
    # Replace spaces, hyphens and underscores in a string
    return partial(re.sub, r'[ _\-]', rep)

def get_page_sharing_tag_list(page, config):
    ''' Return the tags to be shared from a page, formatted for social sharing and excluding
        any tags configured for exclusion '''
    return list(
            filter(lambda x: x not in config.exclude_hashtags,
                map(str.lower, map(strip_seps_fn(), page.meta.get('tags', [])))
            )
        )

def button_name_to_class(name):
    print(strip_seps_fn(' ')(name).capitalize())
    return strip_space_fn()(strip_seps_fn(' ')(name).title()) + "Button"
