# Generated by Django 2.2.5 on 2019-09-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190923_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]