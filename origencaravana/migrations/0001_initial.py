# Generated by Django 3.2.7 on 2021-10-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Origencaravana',
            fields=[
                ('idcaravana', models.AutoField(db_column='IdCaravana', primary_key=True, serialize=False)),
                ('lugar', models.CharField(db_column='Lugar', max_length=60)),
            ],
            options={
                'verbose_name': 'Origen Caravana',
                'verbose_name_plural': 'Origen Caravanas',
            },
        ),
    ]
