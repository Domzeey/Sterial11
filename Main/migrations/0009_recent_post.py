# Generated by Django 4.1.4 on 2022-12-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='Resentpost_pictures')),
            ],
        ),
    ]
