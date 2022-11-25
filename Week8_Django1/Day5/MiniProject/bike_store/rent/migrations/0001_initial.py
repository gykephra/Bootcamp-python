# Generated by Django 4.1.3 on 2022-11-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=200)),
                ('adresse2', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=200)),
                ('code_postal', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.address')),
            ],
        ),
        migrations.CreateModel(
            name='Taille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('cout', models.FloatField()),
                ('taille', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.taille')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.type')),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux', models.FloatField()),
                ('taille_v', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.taille')),
                ('type_v', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.type')),
            ],
        ),
        migrations.CreateModel(
            name='RentalStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('capacité', models.IntegerField()),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.address')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_locat', models.DateField()),
                ('date_retour', models.DateField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.client')),
                ('vehicule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.vehicule')),
            ],
        ),
    ]