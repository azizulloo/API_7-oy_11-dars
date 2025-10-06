from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    founded_year=models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
    
class Color(models.Model):
    name=models.CharField(max_length=50)
    hex_code=models.CharField(max_length=7)  #FFFFFF
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Car(models.Model):
    car_name=models.CharField(max_length=50)
    year=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    max_speed=models.IntegerField()
    engine=models.CharField(max_length=50)  #Benzin yoki Gaz
    
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f"{self.brand.name} {self.car_name}"