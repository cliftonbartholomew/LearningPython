# Generated by Django 3.1.6 on 2021-02-09 15:41

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tagme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
