# Generated by Django 3.2.7 on 2021-10-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('idruta', models.AutoField(db_column='IdRuta', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50, verbose_name='Nombre de la Ruta')),
                ('destino', models.CharField(db_column='Destino', max_length=50)),
            ],
            options={
                'verbose_name': 'Ruta',
                'verbose_name_plural': 'Rutas',
                'db_table': 'ruta',
                'managed': False,
            },
        ),
    ]
