# Generated by Django 4.1.4 on 2022-12-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='Testimonial_pictures')),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonials',
        ),
    ]
