from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(blocks.StructBlock):
    """Cards with image and title and link."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=60)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"