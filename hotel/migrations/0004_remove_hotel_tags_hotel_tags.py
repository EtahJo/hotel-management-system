# Generated by Django 4.2.15 on 2024-08-19 04:48

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('hotel', '0003_alter_hotel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='tags',
        ),
        migrations.AddField(
            model_name='hotel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
