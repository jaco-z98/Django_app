# Generated by Django 4.0.4 on 2022-05-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Klasa A', 'Klasa A'), ('Klasa B', 'Klasa B'), ('Klasa C', 'Klasa C'), ('Klasa D', 'Klasa D'), ('Klasa E', 'Klasa E'), ('Klasa F', 'Klasa F'), ('Klasa S', 'Klasa S'), ('Klasa H', 'Klasa H'), ('Klasa J', 'Klasa J'), ('Klasa M', 'Klasa M')], default=None, max_length=50)),
            ],
            options={
                'verbose_name': 'CarType',
            },
        ),
        migrations.CreateModel(
            name='CarFuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fueltype', models.ForeignKey(choices=[('Olej napędowy', 'Olej napędowy'), ('Benzyna', 'Benzyna'), ('Elektryczny', 'Elektryczny')], on_delete=django.db.models.deletion.CASCADE, to='CarRental.cartype')),
            ],
            options={
                'verbose_name': 'FuelType',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.IntegerField(default=None)),
                ('brand', models.TextField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
                ('fueltype', models.ManyToManyField(to='CarRental.carfueltype')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CarRental.cartype')),
            ],
            options={
                'verbose_name': 'Car',
            },
        ),
    ]