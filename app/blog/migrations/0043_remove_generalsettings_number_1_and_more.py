# Generated by Django 4.0.10 on 2023-05-24 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_remove_article_author_delete_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalsettings',
            name='number_1',
        ),
        migrations.RemoveField(
            model_name='generalsettings',
            name='number_2',
        ),
        migrations.RemoveField(
            model_name='generalsettings',
            name='number_3',
        ),
    ]
