# Generated by Django 5.1.4 on 2024-12-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
