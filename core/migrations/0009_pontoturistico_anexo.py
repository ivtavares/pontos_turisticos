# Generated by Django 2.2.5 on 2019-09-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pontoturistico_fotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='pontos_turisticos_arquivos'),
        ),
    ]