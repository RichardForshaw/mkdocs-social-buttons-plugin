# Twitter button class

from .base import LinkButton

class TwitterButton(LinkButton):
    config_name = "twitter"
    button_url = "https://twitter.com/share?ref_src=twsrc%5Etfw"
    button_style = 'class="twitter-share-button"'

    # Script string:
    button_script = '<script src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    handler_script = '<script type="text/javascript" defer>twttr.ready(twttr.events.bind("click", ev => {{ {function_handler} }}))</script>'

    # Custom attributes
    attr_show_count = "false"

    def generate(self, share_url, hashtags=[]):
        # Override generate to add hashtags
        if len(hashtags):
            self.attr_hashtags = ','.join(hashtags)

        return super(TwitterButton, self).generate(share_url)
