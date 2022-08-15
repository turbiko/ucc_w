import os
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.search import index

from streams import blocks

def file_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    a_filename= 'ucc_'
    return f'files/{a_filename}{file_extension}'


class HomePage(Page):
    logo_text = models.CharField(_('Logotype long'), max_length=50, blank=True)
    logo_abreviation = models.CharField(_('logo abbreviation'), max_length=5, blank=True)
    text_intro = models.TextField(blank=True)
    youtube_video_id = models.CharField(_('Youtube video ID'), max_length=50, blank=True)
    text_prologue_title = models.TextField(blank=True)
    text_prologue = models.TextField(blank=True)
    text_list_why_title = models.TextField(blank=True)
    text_list_why_1 = models.TextField(blank=True)
    text_list_why_2 = models.TextField(blank=True)
    text_list_why_3 = models.TextField(blank=True)
    text_list_why_4 = models.TextField(blank=True)
    text_list_why_5 = models.TextField(blank=True)
    text_list_how_title = models.TextField(blank=True)
    text_list_how_1 = models.TextField(blank=True)
    text_list_how_2 = models.TextField(blank=True)
    text_list_how_3 = models.TextField(blank=True)
    text_list_who_title = models.TextField(blank=True)
    text_list_who_1 = models.TextField(blank=True)
    text_list_who_2 = models.TextField(blank=True)
    text_list_guiding_header = models.TextField(blank=True)
    text_list_guiding_title_1 = models.TextField(blank=True)
    text_list_guiding_1 = models.TextField(blank=True)
    text_list_guiding_title_2 = models.TextField(blank=True)
    text_list_guiding_2 = models.TextField(blank=True)
    text_list_guiding_title_3 = models.TextField(blank=True)
    text_list_guiding_3 = models.TextField(blank=True)
    text_list_guiding_title_4 = models.TextField(blank=True)
    text_list_guiding_4 = models.TextField(blank=True)
    text_list_guiding_title_5 = models.TextField(blank=True)
    text_list_guiding_5 = models.TextField(blank=True)
    text_list_next_title = models.TextField(blank=True)
    text_list_next = models.TextField(blank=True)
    text_partners = models.TextField(blank=True)
    text_copyright = models.TextField(blank=True)

    content = StreamField([
        ("cards", blocks.CardBlock()),
    ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo_abreviation'),
        FieldPanel('logo_text'),
        FieldPanel('text_intro', classname="full"),
        FieldPanel('youtube_video_id'),
        FieldPanel('text_prologue_title'),
        FieldPanel('text_prologue'),
        FieldPanel('text_list_why_title'),
        FieldPanel('text_list_why_1'),
        FieldPanel('text_list_why_2'),
        FieldPanel('text_list_why_3'),
        FieldPanel('text_list_why_4'),
        FieldPanel('text_list_why_5'),
        FieldPanel('text_list_how_title'),
        FieldPanel('text_list_how_1'),
        FieldPanel('text_list_how_2'),
        FieldPanel('text_list_how_3'),
        FieldPanel('text_list_who_title'),
        FieldPanel('text_list_who_1'),
        FieldPanel('text_list_who_2'),
        FieldPanel('text_list_guiding_header'),
        FieldPanel('text_list_guiding_title_1'),
        FieldPanel('text_list_guiding_1'),
        FieldPanel('text_list_guiding_title_2'),
        FieldPanel('text_list_guiding_2'),
        FieldPanel('text_list_guiding_title_3'),
        FieldPanel('text_list_guiding_3'),
        FieldPanel('text_list_guiding_title_4'),
        FieldPanel('text_list_guiding_4'),
        FieldPanel('text_list_guiding_title_5'),
        FieldPanel('text_list_guiding_5'),
        FieldPanel('text_list_next_title'),
        FieldPanel('text_list_next'),
        StreamFieldPanel("content"),
        FieldPanel('text_partners'),
        FieldPanel('text_copyright'),
    ]

