# Generated by Django 2.2.5 on 2019-09-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('njaflights', '0002_auto_20190918_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('njaflights', models.ManyToManyField(blank=True, related_name='passengers', to='njaflights.NjaFlight')),
            ],
        ),
    ]