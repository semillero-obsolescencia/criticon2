# Generated by Django 2.0.3 on 2018-03-14 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(default='Mi Expo', max_length=150)),
                ('desde', models.DateTimeField(auto_now=True)),
                ('hasta', models.DateTimeField(blank=True)),
                ('lugar', models.CharField(blank=True, max_length=150)),
                ('descripcion', models.TextField(blank=True)),
                ('creditos', models.TextField(blank=True)),
                ('texto_curatorial', models.CharField(blank=True, default='', max_length=100)),
                ('rating', models.FloatField(default=2.5)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creador', models.CharField(default='', max_length=150)),
                ('titulo', models.CharField(default='', max_length=150)),
                ('fecha', models.DateField(auto_now=True)),
                ('medio', models.CharField(blank=True, max_length=150)),
                ('descripcion', models.TextField(blank=True)),
                ('rating', models.FloatField(default=2.5)),
                ('likes', models.IntegerField()),
                ('lecturas', models.IntegerField(blank=True, default=0)),
                ('active', models.BooleanField(default=False)),
                ('expo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expos.Expo')),
            ],
            options={
                'ordering': ('creador',),
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pageid', models.CharField(default='index', max_length=50)),
                ('header', models.CharField(blank=True, default='', max_length=150)),
                ('message', models.TextField(blank=True)),
                ('urltext', models.CharField(blank=True, default='', max_length=100)),
                ('project', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='page', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pageid',),
            },
        ),
    ]
