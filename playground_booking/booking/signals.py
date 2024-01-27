from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Booking

@receiver(pre_save, sender=Booking)
def calculate_total_price(sender, instance, **kwargs):
    # Рассчитываем разницу во времени между началом и концом бронирования
    time_difference = instance.end_datetime - instance.start_datetime

    # Преобразуем разницу во времени в количество часов
    hours = time_difference.total_seconds() / 3600

    # Получаем цену за час из соответствующего Playground
    hourly_price = instance.playground.price

    # Рассчитываем общую стоимость
    total_price = hours * hourly_price

    # Устанавливаем значение total_price в модели Booking
    instance.total_price = total_price
