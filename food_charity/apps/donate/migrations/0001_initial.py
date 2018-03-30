# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_name', models.CharField(max_length=80)),
                ('contact_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('admin_level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=80)),
                ('contact_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('admin_level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donor_city', to='donate.City')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=80)),
                ('type_of_food', models.CharField(default='', max_length=80)),
                ('pickup', models.DateField(default='', max_length=8)),
                ('pickup_time', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('charity', models.ManyToManyField(related_name='foods', to='donate.Charity')),
                ('donor', models.ManyToManyField(related_name='foods', to='donate.Donor')),

            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='donor',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donor_state', to='donate.State'),
        ),
        migrations.AddField(
            model_name='charity',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charity_city', to='donate.City'),
        ),
        migrations.AddField(
            model_name='charity',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charity_state', to='donate.State'),
        ),
    ]
