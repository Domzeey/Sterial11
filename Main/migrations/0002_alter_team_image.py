# Generated by Django 4.1.4 on 2022-12-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='Team_pictures'),
        ),
    ]
