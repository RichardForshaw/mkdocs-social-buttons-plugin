# Test basic social button class

from mkdocs_social_buttons_plugin.buttons.base import ButtonBase

import pytest

def test_button_class_without_config_name():
    class BadButton(ButtonBase):
        pass

    with pytest.raises(NotImplementedError) as e_info:
        b = BadButton({})

    assert e_info.value.args[0] == "Missing required attribute: config_name"

def test_button_class_without_button_url():
    class BadButton(ButtonBase):
        config_name = "badbutton"
        pass

    with pytest.raises(NotImplementedError) as e_info:
        b = BadButton({})

    assert e_info.value.args[0] == "Missing required attribute: button_url"
