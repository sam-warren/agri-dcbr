from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


# class Category(models.Model):
#    name = models.CharField(max_length=32)
#    slug = models.SlugField(max_length=32, default="", blank=True)
#    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.name

#    def save(self, *args, **kwargs):
#        self.slug = slugify(self.name)
#        super().save(*args, **kwargs)

#    class Meta:
#        verbose_name_plural = "Categories"


# class Entry(models.Model):
#    title = models.CharField(max_length=64)
#    slug = models.SlugField(max_length=32, default="", blank=True)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
#    content = models.TextField()
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.title

#    def save(self, *args, **kwargs):
#        self.slug = slugify(self.title)
#        super().save(*args, **kwargs)

#    class Meta:
#        verbose_name_plural = "Entries"


class Operator(models.Model):
    regNum = models.CharField(max_length=14)
    firstName = models.CharField(max_length=32)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (self.regNum, self.lastName, self.firstName)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.regNum)
        super().save(*args, **kwargs)
        self.regNum = "BC-DCBR-" + str(self.pk).zfill(6)
        super().save()

    # self.regNum = 'BC ' + str(self.kwargs['pk'])

    class Meta:
        verbose_name_plural = "Operators"


class Address(models.Model):
    PRIMARY = "PRI"
    OPERATION = "OPN"
    VETERINARY = "VET"
    TYPE_CHOICES = (
        (PRIMARY, "Primary"),
        (OPERATION, "Operation"),
        (VETERINARY, "Veterinary"),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=PRIMARY)

    streetNum = models.IntegerField()
    suite = models.CharField(max_length=32, default="", blank=True)
    streetName = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    postalCode = models.CharField(max_length=7)
    province = "BC"
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="addresses"
    )

    def __str__(self):
        return self.streetName

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"
