from django.db import models
from django.contrib.auth.models import User

DAYS_OF_WEEK = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]

class TimeMultiplier(models.Model):
    from_minute = models.PositiveIntegerField()
    to_minute = models.PositiveIntegerField()
    multiplier = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.from_minute}-{self.to_minute}min → {self.multiplier}x"


class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    days_of_week = models.CharField(max_length=100)  # e.g., "Mon,Tue,Wed"
    base_distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    base_price = models.DecimalField(max_digits=7, decimal_places=2)
    additional_price_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    time_multipliers = models.ManyToManyField(TimeMultiplier)
    waiting_free_minutes = models.PositiveIntegerField(default=3)
    waiting_charge_per_3min = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - Active: {self.is_active}"


class ConfigChangeLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    change_summary = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.actor} updated config {self.config.name}"
