from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250) # con el Char es para modificar los caracteres del título
    content=models.TextField()

    def __str__(self):
        return self.title


