# Tests for utils

from mkdocs_social_buttons_plugin import utils

def test_convert_plugin_name_to_class():
    assert utils.button_name_to_class("twitter") == "TwitterButton"
    assert utils.button_name_to_class("linked_in") == "LinkedInButton"

