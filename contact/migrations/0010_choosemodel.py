# Generated by Django 4.1.7 on 2023-05-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_alter_buyurtmaberish_email1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mashina', models.CharField(max_length=100)),
                ('rasm', models.ImageField(upload_to='image/')),
                ('narxi', models.CharField(max_length=50)),
                ('soat', models.PositiveBigIntegerField()),
            ],
        ),
    ]
