# Generated by Django 4.0.10 on 2023-06-20 20:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_generalsettings_mobile_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[410, 410], upload_to='certificate_images'),
        ),
    ]