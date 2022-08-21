from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    class Meta:
        db_table = "students"

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
