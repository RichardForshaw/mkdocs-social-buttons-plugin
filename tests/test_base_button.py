# Test basic social button class

from mkdocs_social_buttons_plugin.buttons.base import ButtonBase, LinkButton, ScriptButton

import pytest

def test_button_class_without_config_name():
    class BadButton(ButtonBase):
        pass

    with pytest.raises(NotImplementedError) as e_info:
        b = BadButton({})

    assert e_info.value.args[0] == "Missing required attribute: config_name"

def test_button_class_without_button_script():
    class BadButton(ButtonBase):
        config_name = "button-missing-script"

    with pytest.raises(NotImplementedError) as e_info:
        b = BadButton({})

    assert e_info.value.args[0] == "Missing required attribute: button_script"

def test_link_button_class_without_button_url():
    class BadButton(LinkButton):
        config_name = "button-missing-url"

    with pytest.raises(NotImplementedError) as e_info:
        b = BadButton({})

    assert e_info.value.args[0] == "Missing required attribute: button_url"
