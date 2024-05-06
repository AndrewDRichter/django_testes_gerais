# Generated by Django 5.0.4 on 2024-05-06 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_usuario_endereco'),
        ('financeiro', '0003_alter_contacliente_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=14, verbose_name='Saldo')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='financeiro.conta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.usuario')),
            ],
            options={
                'verbose_name': 'ContaCliente',
                'verbose_name_plural': 'ContasClientes',
            },
        ),
        migrations.DeleteModel(
            name='ContaCliente',
        ),
    ]
