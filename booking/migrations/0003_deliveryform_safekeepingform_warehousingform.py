# Authored by Alfred_Asare
# Generated by Django 3.0.3 on 2020-02-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0002_auto_20200220_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=30)),
                ('location_from', models.CharField(max_length=150)),
                ('location_to', models.CharField(max_length=150)),
                ('items_list', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='SafeKeepingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=30)),
                ('location_from', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('items_list', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='WareHousingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('name_of_business', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=30)),
                ('location_from', models.CharField(max_length=150)),
                ('items_list', models.CharField(max_length=10000)),
            ],
        ),
    ]
