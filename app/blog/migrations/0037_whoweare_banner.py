# Generated by Django 4.0.10 on 2023-05-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_alter_testimonial_text_alter_whoweare_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='whoweare',
            name='banner',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
