# Generated by Django 4.0.10 on 2023-06-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_alter_certificate_certificate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='whoweare',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Slug'),
        ),
    ]