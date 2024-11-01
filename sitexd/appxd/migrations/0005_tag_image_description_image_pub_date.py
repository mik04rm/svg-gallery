# Generated by Django 5.0.4 on 2024-05-20 12:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appxd', '0004_rectangle_fill_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]