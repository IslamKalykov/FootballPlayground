from django.contrib import admin
from .models import CustomUser, Playground, Booking

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role', 'is_active', 'created_date')
    search_fields = ('first_name', 'last_name')
    ordering = ('-created_date',)
    
admin.site.register(CustomUser, CustomUserAdmin)

# Создаем класс для кастомизации отображения Playground в админ-панели
class PlaygroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'admin', 'address', 'price', 'width', 'height', 'reservation_status', 'is_active')
    search_fields = ('name', 'admin__username', 'address')
    list_filter = ('reservation_status', 'is_active')
    ordering = ('-created_date',)

# Регистрируем модель Playground с кастомным классом в админ-панели
admin.site.register(Playground, PlaygroundAdmin)

# Создаем класс для кастомизации отображения Booking в админ-панели
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'playground', 'user', 'start_datetime', 'end_datetime', 'is_confirmed', 'admin_status', 'total_price')
    search_fields = ('playground__name', 'user__username', 'start_datetime', 'end_datetime')
    list_filter = ('is_confirmed', 'admin_status')
    ordering = ('-created_date',)
    actions = ['approve_selected_bookings', 'reject_selected_bookings', 'pending_selected_bookings']

    def approve_selected_bookings(modeladmin, request, queryset):
        queryset.update(admin_status='approved', is_confirmed=True)

    def reject_selected_bookings(modeladmin, request, queryset):
        queryset.update(admin_status='rejected', is_confirmed=False)
        
    def pending_selected_bookings(modeladmin, request, queryset):
        queryset.update(admin_status='pending', is_confirmed=False)
        
# Регистрируем модель Booking с кастомным классом в админ-панели
admin.site.register(Booking, BookingAdmin)
