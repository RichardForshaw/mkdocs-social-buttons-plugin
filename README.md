# mkdocs-social-buttons-plugin
A plugin to provide basic social button sharing to MKDocs pages

This plugin allows social sharing buttons to be added to the mkdocs.yml file, which will then build buttons into the site pages.

## Basic

The plugin defines the buttons in the mkdocs.yml file. This example shows the simplest settings

```
plugins:
    - social-buttons:
        default_message: "A default message"
        apply_to_paths:
          - blog/path
        exclude_hashtags:
          - guestauthor
        twitter:
          message: "A button specific message"
```

A section is defined under `social-buttons` for each button that you wish to add. The settings for generating the buttons are as follows:

 * `default_message`: A sharing message that applies to all buttons (the text to be shared with)
 * `<button>/message`: A specific message to be used for the given button. This overrides the default message
 * `alternative_url_root`: An alternative URL to use as the sharing root in the links (e.g. `http://mytesturl.com/`)
 * `apply_to_paths`: a list of paths to apply the buttons to (e.g. you only want to apply them to the blog content). If not present, applies to all pages.
 * `exclude_hashtags`: if you use the meta property `tags`, exclude the hashtags listed from the share text (note they are listed in hashtag-format with no spaces)

## Styling buttons

The buttons are generated as list items, so they can be styled conveniently. The list styling is up to the user, generally to allow control of flow and padding etc.

The following config items are available to assist with styling:

 * `button_class`: A class that is rendered as the list item's class, i.e. `<li class="<named class>">`
 * `button_style`: A style that is rendered as the list item's style, i.e. `<li style="<named class>">`

## Available buttons

Current supported buttons are:

 * Twitter: config section name: `twitter`
 * LinkedIn: config section name: `linked_in`
