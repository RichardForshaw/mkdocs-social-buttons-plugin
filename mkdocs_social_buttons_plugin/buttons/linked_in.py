# LinkedIn button class

from .base import ScriptButton

class LinkedInButton(ScriptButton):
    config_name = "linkedin"
    script_type = "IN/Share"
    button_script = '<script src="https://platform.linkedin.com/in.js" type="text/javascript">lang: en_US</script>'
