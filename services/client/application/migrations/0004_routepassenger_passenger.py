# Generated by Django 2.2.5 on 2019-10-04 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20190923_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='routepassenger',
            name='passenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.Passenger'),
            preserve_default=False,
        ),
    ]
