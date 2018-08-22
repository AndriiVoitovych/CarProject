from django.contrib import admin

from .models import Car, Service, ServiceHistory

admin.site.register(Service)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mileage')


@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('current_mileage',)
