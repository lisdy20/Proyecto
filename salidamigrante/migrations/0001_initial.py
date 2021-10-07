# Generated by Django 3.2.7 on 2021-10-01 20:27

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
                ('fechasalida', models.DateTimeField(db_column='FechaSalida')),
            ],
            options={
                'db_table': 'salidamigrante',
                'managed': False,
            },
        ),
    ]
