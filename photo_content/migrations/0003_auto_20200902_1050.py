# Generated by Django 3.1 on 2020-09-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_content', '0002_auto_20200902_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='photographer',
            field=models.CharField(default='Jasmine Moore', max_length=200),
            preserve_default=False,
        ),
    ]
