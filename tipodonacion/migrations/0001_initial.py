# Generated by Django 3.2.7 on 2021-10-15 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo', '0001_initial'),
        ('donacion', '0002_alter_donacion_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipodonacion',
            fields=[
                ('idtipodonacion', models.AutoField(db_column='IdTipoDonacion', primary_key=True, serialize=False)),
                ('item', models.CharField(db_column='Item', max_length=100, verbose_name='Artículo/Item')),
                ('cantidad', models.IntegerField(db_column='Cantidad')),
                ('donacion', models.ForeignKey(db_column='FkIdDonacion', on_delete=django.db.models.deletion.DO_NOTHING, to='donacion.donacion')),
                ('nombre', models.ForeignKey(db_column='FkIdTipo', on_delete=django.db.models.deletion.DO_NOTHING, to='tipo.tipo')),
            ],
            options={
                'verbose_name': 'Detalle de Donación',
                'verbose_name_plural': 'Detalle de Donaciones',
            },
        ),
    ]
