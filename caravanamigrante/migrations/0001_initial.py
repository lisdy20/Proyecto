# Generated by Django 3.2.7 on 2021-10-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caravanamigrante',
            fields=[
                ('idcaravana', models.AutoField(db_column='IdCaravana', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
            ],
            options={
                'db_table': 'caravanamigrante',
                'managed': False,
            },
        ),
    ]
