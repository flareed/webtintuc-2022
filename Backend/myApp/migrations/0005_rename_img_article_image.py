# Generated by Django 4.1.3 on 2022-12-15 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_category_articles_alter_article_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img',
            new_name='image',
        ),
    ]
