# Generated by Django 4.2.2 on 2023-09-23 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Number of guests')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='No category', max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category_image/', verbose_name='Category_icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Name product')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='product_image/', verbose_name='Photo product')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price for person')),
                ('number_of_guests', models.PositiveSmallIntegerField(blank=True, default=1, null=True, verbose_name='Minimal number of guests')),
                ('available', models.BooleanField(default=True, verbose_name='Availability')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_Category', to='store.category', verbose_name='Category product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WorkDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_day', models.CharField(blank=True, choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday '), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='MONDAY', max_length=100, null=True)),
                ('beginning_of_work_day_time', models.TimeField(default=datetime.time(8, 0), verbose_name='Beginning of work time')),
                ('end_of_work_day_time', models.TimeField(default=datetime.time(20, 0), verbose_name='End of work time')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name': 'day',
                'verbose_name_plural': 'days',
            },
        ),
    ]