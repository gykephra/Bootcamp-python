# Generated by Django 4.1.3 on 2022-11-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(null=True)),
            ],
        ),
    ]
