from django import template


register = template.Library()


@register.simple_tag
def calculate_next_service(service, car):
    current_mileage = car.mileage
    ret = 0

    try:
        last_history_entry = car.servicehistory_set.filter(service=service).last()
        ret = current_mileage - last_history_entry.current_mileage - service.period
    except:
        ret = current_mileage - service.period

    return ret * -1
