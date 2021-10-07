# Generated by Django 3.2.7 on 2021-10-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipodonacion',
            fields=[
                ('idtipodonacion', models.AutoField(db_column='IdTipoDonacion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=75, verbose_name='Tipo')),
                ('cantidad', models.IntegerField(db_column='Cantidad')),
            ],
            options={
                'verbose_name': 'Tipo de Donación',
                'verbose_name_plural': 'Tipo de Donaciones',
                'db_table': 'tipodonacion',
                'managed': False,
            },
        ),
    ]
