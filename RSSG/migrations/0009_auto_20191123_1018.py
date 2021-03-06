# Generated by Django 2.2.5 on 2019-11-23 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RSSG', '0008_alpha_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='context',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='history'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='year',
            field=models.CharField(default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]
