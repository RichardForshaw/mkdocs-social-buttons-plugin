# Tests for twitter HTML generation

from mkdocs_social_buttons_plugin.buttons.twitter import TwitterButton

from collections import namedtuple

TWITTER_SCRIPT = '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

def test_generate_basic_twitter_button_HTML():
    test_obj = TwitterButton({})

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared from MKDocs" data-url="http://testurl.com" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com") == expected

def test_generate_twitter_button_HTML_with_default_message():
    plugin_config = { 'default_message': "Shared with default message"}
    test_obj = TwitterButton(plugin_config)

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared with default message" data-url="http://testurl.com" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com") == expected

    # Test also when there is an empty button config
    plugin_config = { 'default_message': "Shared with default message", 'twitter': {}}
    test_obj2 = TwitterButton(plugin_config)
    assert test_obj2.generate("http://testurl.com") == expected

def test_generate_twitter_button_HTML_with_button_message():
    plugin_config = { 'twitter': {'message': "Shared with custom message"}}
    test_obj = TwitterButton(plugin_config)

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared with custom message" data-url="http://testurl.com" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com") == expected

def test_generate_twitter_button_HTML_with_overridden_message():
    plugin_config = {
        'default_message': "Shared with default message",
        'twitter': {'message': "Shared with overridden message"}
        }
    test_obj = TwitterButton(plugin_config)

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared with overridden message" data-url="http://testurl.com" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com") == expected

def test_generate_twitter_button_with_hashtag():
    test_obj = TwitterButton({})

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared from MKDocs" data-url="http://testurl.com" data-hashtags="hashtag1" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com", ['hashtag1']) == expected

def test_generate_twitter_button_with_multiple_hashtags():
    test_obj = TwitterButton({})

    expected = '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="Shared from MKDocs" data-url="http://testurl.com" data-hashtags="hashtag1,hashtag2,hashtag3" data-show-count="false"></a>'
    assert test_obj.generate("http://testurl.com", ['hashtag1', 'hashtag2', 'hashtag3']) == expected

def test_get_script():
    test_obj = TwitterButton({})
    assert test_obj.get_script() == '<script src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

def test_get_script_with_share_handler():
    plugin_config = { 'twitter': { 'button_share_callback': 'function'}}
    mock_page = namedtuple('Page', 'abs_url')('path/to/page')
    test_obj = TwitterButton(plugin_config)

    expected = '<script src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>' + \
        '<script type="text/javascript" defer>twttr.ready(twttr.events.bind("click", ev => { function("path/to/page", "twitter") }))</script>'
    assert test_obj.get_script(mock_page) == expected
