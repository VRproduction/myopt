# Generated by Django 4.2 on 2023-04-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_remove_generalsettings_comment_user_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalsettings',
            name='twitter',
        ),
    ]
