# Generated by Django 5.0.6 on 2024-05-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtWork', '0002_alter_artwork_pigment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='DecayStatus',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]