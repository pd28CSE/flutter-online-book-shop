# Generated by Django 4.1.7 on 2023-03-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('edition', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to='books')),
                ('image1', models.ImageField(upload_to='books')),
                ('image2', models.ImageField(upload_to='books')),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
