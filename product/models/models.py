from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name    = "Urun"
        verbose_name_plural    = "Urunler"

