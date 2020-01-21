# Generated by Django 3.0.1 on 2020-01-13 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=20)),
                ('id_perfil', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Perfil')),
            ],
        ),
    ]