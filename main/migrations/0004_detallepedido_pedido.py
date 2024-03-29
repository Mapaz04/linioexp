# Generated by Django 3.2.3 on 2021-05-22 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cliente_colaborador_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(max_length=3)),
                ('direccion_entrega', models.CharField(blank=True, max_length=100, null=True)),
                ('tarifa', models.FloatField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('repartidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producto')),
            ],
        ),
    ]
