# Generated by Django 3.2.3 on 2021-06-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210618_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoszapatilla',
            name='fecha',
            field=models.CharField(max_length=10, verbose_name='Fecha'),
        ),
    ]