# Generated by Django 5.0.6 on 2024-05-27 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtWork', '0006_image_f_number_image_imagesource_image_inventorynr_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='artwork',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtWork.image'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='Artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtWork.artist'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
