# Generated by Django 5.0.2 on 2024-02-23 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quarto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicial', models.DateField()),
                ('dt_final', models.DateField()),
                ('idclient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('idquarto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quarto.quarto')),
            ],
        ),
    ]
