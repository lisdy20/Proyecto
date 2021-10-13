# Generated by Django 3.2.7 on 2021-10-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.AutoField(db_column='IdPais', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50, verbose_name='País')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
    ]
