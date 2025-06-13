from django.contrib import admin
from .models import PricingConfig, TimeMultiplier, ConfigChangeLog

# Admin for TimeMultiplier
@admin.register(TimeMultiplier)
class TimeMultiplierAdmin(admin.ModelAdmin):
    list_display = ('from_minute', 'to_minute', 'multiplier')
    ordering = ('from_minute',)


# Admin for PricingConfig
@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'days_of_week', 'base_distance_km', 'base_price')
    list_filter = ('is_active',)
    search_fields = ('name', 'days_of_week')
    filter_horizontal = ('time_multipliers',)


# Admin for Config Change Log
@admin.register(ConfigChangeLog)
class ConfigChangeLogAdmin(admin.ModelAdmin):
    list_display = ('config', 'actor', 'timestamp')
    search_fields = ('config__name', 'actor__username')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
