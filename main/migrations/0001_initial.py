# Generated by Django 4.1.7 on 2023-05-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.CharField(default='2022-02-22', max_length=20)),
                ('event_name', models.CharField(default='NoName', max_length=128)),
                ('location', models.CharField(default='None', max_length=38)),
                ('tickets_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Events',
            },
        ),
    ]