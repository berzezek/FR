# Generated by Django 4.1.4 on 2023-02-02 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=32, unique=True)),
                ('phone_prefix', models.CharField(max_length=32)),
                ('tag', models.CharField(max_length=128)),
                ('customer_time_zone', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_launch_date', models.DateTimeField()),
                ('end_launch_date', models.DateTimeField()),
                ('customer_filter', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ManyToManyField(blank=True, related_name='customers', to='newsletter.customer')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.newsletter')),
            ],
        ),
    ]
