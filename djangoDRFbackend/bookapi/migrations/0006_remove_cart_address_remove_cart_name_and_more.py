# Generated by Django 4.1.7 on 2023-03-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0005_cart_address_cart_name_cart_phonenum_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='address',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='phoneNum',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='sfsfs', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phoneNum',
            field=models.CharField(default='242424', max_length=15),
            preserve_default=False,
        ),
    ]
