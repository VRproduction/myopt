# Generated by Django 4.0.10 on 2023-06-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_image',
            field=models.ImageField(blank=True, help_text='W: 410, H: 410', null=True, upload_to='certificate_images', verbose_name='image'),
        ),
    ]
