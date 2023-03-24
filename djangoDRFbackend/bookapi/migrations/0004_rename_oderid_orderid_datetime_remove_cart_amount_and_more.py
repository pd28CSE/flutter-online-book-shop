# Generated by Django 4.1.7 on 2023-03-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0003_alter_orderid_oderid_alter_user_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderid',
            old_name='oderId',
            new_name='dateTime',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
