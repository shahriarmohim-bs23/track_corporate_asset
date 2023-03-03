# Generated by Django 4.1.7 on 2023-03-03 14:07

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('Phone', 'Phone'), ('Tablet', 'Tablet'), ('Laptop', 'Laptop'), ('Other', 'Other')], max_length=10)),
                ('purchase_date', models.DateField()),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_date', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateTimeField(blank=True, null=True)),
                ('check_out_condition', models.CharField(blank=True, max_length=100, null=True)),
                ('check_in_condition', models.CharField(blank=True, max_length=100, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]
