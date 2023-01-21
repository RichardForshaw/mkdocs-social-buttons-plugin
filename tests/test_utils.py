# Tests for utils

from mkdocs_social_buttons_plugin import utils

from collections import namedtuple

mock_config = namedtuple('MockConfig', 'exclude_hashtags')
mock_page   = namedtuple('MockPage', 'meta')

def test_convert_plugin_name_to_class():
    assert utils.button_name_to_class("twitter") == "TwitterButton"
    assert utils.button_name_to_class("linked_in") == "LinkedInButton"

def test_get_page_share_tag_list():
    ''' Get a page-share tag list for the page'''
    config = mock_config(['hashtag1', 'hashtag2'])
    page = mock_page({'tags': ['Hashtag1', 'Hash Tag 2', 'Hash-tag3']})
    assert utils.get_page_sharing_tag_list(page, config) == ['hashtag3',]

    config = mock_config(['hashtag2'])
    page = mock_page({'tags': ['Hashtag1', 'Hash Tag 2', 'Hash-tag3']})
    assert utils.get_page_sharing_tag_list(page, config) == ['hashtag1', 'hashtag3']

def test_get_page_share_tag_list_all_excluded():
    config = mock_config(['hashtag1', 'hashtag2'])
    page = mock_page({'tags': ['Hashtag1', 'Hash Tag 2']})
    assert utils.get_page_sharing_tag_list(page, config) == []
