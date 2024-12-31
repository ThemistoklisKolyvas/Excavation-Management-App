# Generated by Django 5.1.4 on 2024-12-28 22:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Excavation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ditch_number', models.CharField(max_length=100)),
                ('pottery', models.BooleanField(default=False)),
                ('jewellery', models.BooleanField(default=False)),
                ('bones', models.BooleanField(default=False)),
                ('tools', models.BooleanField(default=False)),
                ('small_findings', models.BooleanField(default=False)),
                ('samples', models.BooleanField(default=False)),
                ('east_dimension', models.FloatField()),
                ('north_dimension', models.FloatField()),
                ('depth', models.FloatField()),
                ('graves_found', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grave_number', models.CharField(max_length=100, unique=True)),
                ('comments', models.TextField()),
                ('east_dimension', models.FloatField()),
                ('north_dimension', models.FloatField()),
                ('depth', models.FloatField()),
                ('excavation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graves', to='the_excavation.excavation')),
            ],
        ),
    ]
