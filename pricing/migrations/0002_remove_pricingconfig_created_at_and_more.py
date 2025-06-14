# Generated by Django 5.1.2 on 2025-06-13 07:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingconfig',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='timemultiplier',
            name='config',
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='time_multipliers',
            field=models.ManyToManyField(to='pricing.timemultiplier'),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='additional_price_per_km',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='base_distance_km',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='base_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='days_of_week',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='waiting_charge_per_3min',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='timemultiplier',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.CreateModel(
            name='ConfigChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('change_summary', models.TextField()),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.pricingconfig')),
            ],
        ),
        migrations.DeleteModel(
            name='PricingLog',
        ),
    ]
