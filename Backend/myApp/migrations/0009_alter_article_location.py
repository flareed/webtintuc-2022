# Generated by Django 4.1.3 on 2022-12-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_article_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]