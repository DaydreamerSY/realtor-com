# Generated by Django 3.0.3 on 2022-05-15 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_realestatepost_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestatepost',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='real_estate_posts', to='api.Region'),
        ),
    ]
