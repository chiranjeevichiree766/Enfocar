from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PricingConfig
from decimal import Decimal

@api_view(['POST'])
def calculate_prices(request):
    try:
        day = request.data.get('day')  # e.g., "Mon"
        total_distance = Decimal(str(request.data.get('distance')))
        ride_time = int(request.data.get('ride_time'))
        waiting_time = int(request.data.get('waiting_time'))

        config = PricingConfig.objects.filter(is_active=True, days_of_week__icontains=day).first()
        if not config:
            return Response({"error": "No active pricing config for this day."}, status=404)

        base_km = Decimal(config.base_distance_km)
        base_price = config.base_price  # DBP
        additional_km = max(Decimal('0'), total_distance - base_km)
        
        additional_price = additional_km * config.additional_price_per_km # Dn * DAP

        multiplier = Decimal('1.0')
        for tm in config.time_multipliers.all():
            if tm.from_minute <= ride_time <= tm.to_minute:
                multiplier = tm.multiplier 
                break

        waiting_extra = max(0, waiting_time - config.waiting_free_minutes)
        waiting_units = waiting_extra // 3
        waiting_charge = Decimal(waiting_units) * config.waiting_charge_per_3min # WC

        price = ((base_price + additional_price) * multiplier) + waiting_charge

        return Response({
            "price": round(price, 2),
            "breakdown": {
                "base_price": float(base_price),
                "additional_price": float(additional_price),
                "multiplier": float(multiplier),
                "waiting_charge": float(waiting_charge)
            }
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)
