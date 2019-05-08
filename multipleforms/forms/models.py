from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.message}'
