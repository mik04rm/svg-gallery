# Generated by Django 5.0.4 on 2024-05-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appxd', '0003_image_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='rectangle',
            name='fill_color',
            field=models.CharField(default='#0000FF', max_length=7),
        ),
    ]
