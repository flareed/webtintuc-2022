# Generated by Django 4.1.3 on 2022-12-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
