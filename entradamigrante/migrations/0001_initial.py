# Generated by Django 3.2.7 on 2021-10-15 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo', '0001_initial'),
        ('migrante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entradamigrante',
            fields=[
                ('idmovilidad', models.AutoField(db_column='IdMovilidad', primary_key=True, serialize=False)),
                ('fechaentrada', models.DateTimeField(db_column='FechaEntrada', verbose_name='Fecha de Entrada')),
                ('checkout', models.BooleanField(default=False, verbose_name='Ha marcado salida?')),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=254, null=True, verbose_name='Descripción')),
                ('migrante', models.ForeignKey(db_column='FkIdMigrante', on_delete=django.db.models.deletion.DO_NOTHING, to='migrante.migrante')),
                ('módulo', models.ForeignKey(db_column='FkIdModulo', on_delete=django.db.models.deletion.DO_NOTHING, related_name='modulo', to='modulo.modulo')),
            ],
            options={
                'verbose_name': 'Entrada Migrante',
                'verbose_name_plural': 'Entrada Migrantes',
            },
        ),
    ]
