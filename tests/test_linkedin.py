# Tests for linkedin button

from mkdocs_social_buttons_plugin.buttons.linked_in import LinkedInButton

def test_generate_basic_linkedin_button_HTML():
    test_obj = LinkedInButton({})

    expected = '<script type="IN/Share" data-url="https://testurl.com"></script>'
    assert test_obj.generate("https://testurl.com") == expected


def test_get_script():
    test_obj = LinkedInButton({})
    assert test_obj.get_script() == '<script src="https://platform.linkedin.com/in.js" type="text/javascript">lang: en_US</script>'
