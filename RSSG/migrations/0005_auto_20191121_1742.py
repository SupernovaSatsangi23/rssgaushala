# Generated by Django 2.2.5 on 2019-11-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSSG', '0004_auto_20191121_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image_array_3',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_array_4',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
