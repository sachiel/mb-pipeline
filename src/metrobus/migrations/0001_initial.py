# Generated by Django 3.0.6 on 2020-05-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_date', models.DateTimeField(auto_now_add=True, verbose_name='Modificado')),
                ('record_id', models.CharField(max_length=128, verbose_name='Record ID')),
                ('vehicle_id', models.CharField(blank=True, default='', max_length=64, verbose_name='Vehicle ID')),
                ('trip_id', models.CharField(blank=True, default='', max_length=64, verbose_name='Trip ID')),
                ('trip_route_id', models.CharField(blank=True, default='', max_length=64, verbose_name='Trip Route ID')),
                ('trip_schedule_relationship', models.CharField(blank=True, default='', max_length=64, verbose_name='Trip Schedule Relationship')),
                ('vehicle_label', models.CharField(blank=True, default='', max_length=64, verbose_name='Vehicle Label')),
                ('vehicle_current_status', models.SmallIntegerField(default=0, verbose_name='Vehicle Current Status')),
                ('position_longitude', models.CharField(blank=True, default='', max_length=64, verbose_name='Trip Schedule Relationship')),
                ('position_latitude', models.CharField(blank=True, default='', max_length=64, verbose_name='Trip Schedule Relationship')),
                ('position_speed', models.FloatField(default=0, verbose_name='Vehicle Current Status')),
                ('position_odometer', models.FloatField(default=0, verbose_name='Vehicle Current Status')),
                ('trip_start_date', models.DateField(blank=True, null=True, verbose_name='Start Trip Date')),
                ('date_updated', models.DateTimeField(blank=True, null=True, verbose_name='Record Update')),
                ('is_georeversed', models.BooleanField(default=False, verbose_name='Is georeversed?')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
    ]
