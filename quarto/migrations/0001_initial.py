# Generated by Django 5.0.2 on 2024-02-23 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id_quarto', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('idcategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria')),
            ],
        ),
    ]
