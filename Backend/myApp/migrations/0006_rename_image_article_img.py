# Generated by Django 4.1.3 on 2022-12-15 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_rename_img_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='img',
        ),
    ]
