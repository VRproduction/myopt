# Generated by Django 4.0.10 on 2023-05-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_generalsettings_youtube'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalsettings',
            old_name='linkedin',
            new_name='tiktok',
        ),
    ]
