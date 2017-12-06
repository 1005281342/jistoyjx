from django.db import models

# Create your models here.
class bookInfo(models.Model):
    title = models.CharField(max_length=20 )
    pubData=models.DateField()

    def __str__(self):
        return self.title

class heroInfo(models.Model):
    name = models.CharField(max_length=10 )
    content = models.CharField(max_length=100 )
    gender = models.BooleanField(default=True )
    book = models.ForeignKey(bookInfo )

    def __str__(self):
        return self.name
