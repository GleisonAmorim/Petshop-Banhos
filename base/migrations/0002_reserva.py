# Generated by Django 4.2.9 on 2024-01-17 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('dia_reserva', models.DateField()),
                ('observacoes', models.TextField()),
            ],
        ),
    ]
