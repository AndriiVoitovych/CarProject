from django.db import models


class Car(models.Model):
    DIESEL = 'D'
    PETROL = 'P'
    LPG = 'L'

    FUEL_TYPE_CHOICES = (
        (DIESEL, 'Diesel'),
        (PETROL, 'Petrol'),
        (LPG, 'LPG')
    )

    brand = models.CharField(max_length=30)
    model_name = models.CharField(max_length=200, verbose_name='model')
    product_year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()

    fuel_type = models.CharField(
        max_length=1,
        choices=FUEL_TYPE_CHOICES,
        default=PETROL,
    )

    def __str__(self):
        return self.brand + " " + self.model_name


class Service(models.Model):
    name = models.CharField(max_length=200)
    period = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ServiceHistory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    current_mileage = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Service histories'
        ordering = ('current_mileage',)

    def save(self, *args, **kwargs):
        self.current_mileage = self.car.mileage
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s - %s - %skm' % (self.service, self.car, self.current_mileage)
