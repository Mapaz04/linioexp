# Generated by Django 3.1.7 on 2021-06-05 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_detallepedido_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.producto')),
            ],
        ),
    ]
