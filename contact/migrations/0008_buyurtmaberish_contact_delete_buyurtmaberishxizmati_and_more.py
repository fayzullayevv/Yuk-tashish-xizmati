# Generated by Django 4.1.7 on 2023-05-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_buyurtmaberishxizmati_email1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyurtmaBerish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzildan', models.CharField(max_length=300)),
                ('manzilga', models.CharField(max_length=300)),
                ('email1', models.EmailField(max_length=254)),
                ('raqam1', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('raqam', models.CharField(max_length=70)),
                ('xabar', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='BuyurtmaBerishXizmati',
        ),
        migrations.DeleteModel(
            name='ContactModel',
        ),
    ]
