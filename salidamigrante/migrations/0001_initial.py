# Generated by Django 3.2.7 on 2021-10-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salidamigrante',
            fields=[
                ('idsalida', models.AutoField(db_column='IdSalida', primary_key=True, serialize=False)),
                ('fechasalida', models.DateTimeField(db_column='FechaSalida', verbose_name='Fecha de Salida')),
            ],
            options={
                'verbose_name': 'Salida de Migrante',
                'verbose_name_plural': 'Salidas de Migrante',
                'db_table': 'salidamigrante',
                'managed': False,
            },
        ),
    ]
