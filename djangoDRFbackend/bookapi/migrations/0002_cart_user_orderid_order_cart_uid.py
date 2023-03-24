# Generated by Django 4.1.7 on 2023-03-10 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0.0)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.UUIDField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oderId', models.UUIDField(unique=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.orderid')),
                ('products', models.ManyToManyField(to='bookapi.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.user'),
        ),
    ]