# Generated by Django 5.0.4 on 2024-05-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appxd', '0005_tag_image_description_image_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='appxd.tag'),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]