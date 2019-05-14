from django.db import models

# Create your models here.
class Operator(models.Model):
      name = models.CharField(max_length=40)
      address1 = models.CharField(max_length=200)
      timestamp = models.DateTimeField()
      numDogs = models.IntegerField()
      numCats = models.IntegerField()
      completed = models.BooleanField(default=False)


      def _str_(self):
        return self.name