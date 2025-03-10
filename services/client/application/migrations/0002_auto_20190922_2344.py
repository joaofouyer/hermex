# Generated by Django 2.2.5 on 2019-09-22 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Other'), (1, 'Boundaries'), (2, 'Route Shape')], default=0)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.IntegerField(choices=[(0, 'Other'), (1, 'Go'), (2, 'Back')], default=0)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='application.Driver')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='address',
            new_name='company',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='garage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_garage', to='application.Location'),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Other'), (1, 'Uber Movement')], default=0)),
                ('name', models.CharField(max_length=127)),
                ('number', models.IntegerField(blank=True)),
                ('district_name', models.CharField(blank=True, max_length=127, null=True)),
                ('district_number', models.IntegerField(blank=True, null=True)),
                ('city_name', models.CharField(blank=True, max_length=127, null=True)),
                ('city_number', models.IntegerField(blank=True, null=True)),
                ('movement_id', models.CharField(blank=True, max_length=127, null=True)),
                ('geometry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='zone_geometry', to='application.Geometry')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Pick-up'), (1, 'Drop-off')], default=0)),
                ('time', models.TimeField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Route')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='application.Stop')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='RoutePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='application.Geometry')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='RoutePassenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop_off', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passenger_dropoff', to='application.RouteStop')),
                ('pick_up', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passenger_pickup', to='application.RouteStop')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='route',
            name='path',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='application.RoutePath'),
        ),
        migrations.AddField(
            model_name='route',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='application.Vehicle'),
        ),
        migrations.AddField(
            model_name='coordinates',
            name='geometry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.Geometry'),
        ),
        migrations.AddField(
            model_name='location',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='address_zone', to='application.Zone'),
        ),
    ]
