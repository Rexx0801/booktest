from django.db import models

class Book(models.Model):
    name = models.CharField(max_length= 200)
    amount = models.FloatField()
    detail = models.TextField(max_length=50000)
    image = models.ImageField(upload_to='image')
    nhaxuatban = models.CharField(max_length=100)
    tacgia = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.name