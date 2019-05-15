from django.db import models

# Create your models here.
class Operator(models.Model):
      regNum = models.IntegerField()
      firstName = models.CharField(max_length=50)
      middleName = models.CharField(max_length=50)
      lastName = models.CharField(max_length=50)
      streetNum = models.CharField(max_length=50)
      aptNum = models.IntegerField()
      streetName = models.CharField(max_length=50)
      city = models.CharField(max_length=50)
      postalCode = models.CharField(max_length=50)
      province = models.CharField(max_length=2, default='BC')
      phoneNum = models.CharField(max_length=50)
      email = models.CharField(max_length=50)
      timestamp = models.DateTimeField()
      completed = models.BooleanField(default=False)

      def _str_(self):
        return self.regNum