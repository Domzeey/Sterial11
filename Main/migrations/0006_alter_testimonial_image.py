# Generated by Django 4.1.4 on 2022-12-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]