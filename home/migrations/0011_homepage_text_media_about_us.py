# Generated by Django 4.0.7 on 2022-08-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homepage_text_copyright_homepage_text_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='text_media_about_us',
            field=models.TextField(blank=True),
        ),
    ]
