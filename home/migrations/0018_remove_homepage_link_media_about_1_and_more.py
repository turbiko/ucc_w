# Generated by Django 4.0.7 on 2022-08-15 21:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_homepage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='link_media_about_1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='link_media_about_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='link_media_about_3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_title_1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_title_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pic_media_about_title_3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='text_media_about_pic_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='text_media_about_us',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]