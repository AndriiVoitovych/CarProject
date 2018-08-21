from django.db import models

# Create your models here.
class Car(models.Model):
    DIESEL = 'D'
    PETROL = 'P'
    LPG = 'L'

    FUEL_TYPE_CHOICES = (
        (DIESEL, 'Diesel'),
        (PETROL, 'Petrol'),
        (LPG, 'LPG')
    )

    brand = models.CharField(max_length = 200)
    model = models.CharField(max_length = 200)
    product_date = models.DateField('product date')

    fuel_type = models.CharField(
        max_length=1,
        choices=FUEL_TYPE_CHOICES,
        default=PETROL,
    )

    def str(self):
        return self.brand + " " + self.model

class MileageHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    date = models.DateField()

    def str(self):
        return str(self.mileage) + " " + str(self.date)