# Generated by Django 4.1.4 on 2022-12-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='Testimonials_pictures')),
            ],
        ),
    ]