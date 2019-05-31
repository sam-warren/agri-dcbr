from django.db import models
from django.core.validators import URLValidator

# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User


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

    EMAIL = "Email"
    MAIL = "Mail"

    BREEDER = "BREEDER"
    SELLER = "SELLER"
    BOTH = "BREEDER & SELLER"
    OPERATOR_TYPE_CHOICES = (
        (BREEDER, "breeder"),
        (SELLER, "seller"),
        (BOTH, "breeder & seller"),
    )

    regNum = models.CharField(max_length=14)
    firstName = models.CharField(max_length=32)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    CONTACT_METHOD_CHOICE = ((EMAIL, "email"), (MAIL, "mail"))
    type = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICE, default=EMAIL)
    operator_type = models.CharField(max_length=20, choices=OPERATOR_TYPE_CHOICES, default=BREEDER)

    operationName = models.CharField(max_length=32, default="", blank=True)

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
    province = models.CharField(max_length=2, default="BC")
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


class Risk_Factor_MetaData(models.Model):

    DOG = "DOG"
    CAT = "CAT"
    BOTH = "DOG & CAT"
    OPERATOR_TYPE_CHOICES = (
        (DOG, "dog"),
        (CAT, "cat"),
        (BOTH, "dog & cat"),
    )

    TATTOO = "TATTOO"
    MICROCHIP = "MICROCHIP"
    OTHER = "OTHER"
    PERMANENT_ID_CHOICES = (
        (TATTOO, "tattoo"),
        (MICROCHIP, "microchip"),
        (OTHER, "other"),
    )

    accidental_breeding = models.BooleanField(default=False)
    num_workers = models.IntegerField()
    opn_URL = models.TextField(validators=[URLValidator()])
    num_breeds_dogs = models.IntegerField()
    num_breeds_cats = models.IntegerField()
    has_vet = models.BooleanField(default=False)
    has_perm_id = models.BooleanField(default=False)
    perm_id_type = models.CharField(max_length=10, choices=PERMANENT_ID_CHOICES, default=TATTOO)
    perm_id_other = models.CharField(max_length= 10, default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="riskmetadata"
    )

    def __str__(self):
        return self.operator_type

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RiskFactorsMeta"

class Risk_Factor_Data(models.Model):

    num_dogs_intact = models.IntegerField(default=0)
    num_litter_whelped = models.IntegerField(default=0)
    num_cats_intact = models.IntegerField(default=0)
    num_litter_queened = models.IntegerField(default=0)

    num_sold = models.IntegerField(default=0)
    num_transferred = models.IntegerField(default=0)
    num_traded = models.IntegerField(default=0)
    num_leased = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="risk_data"
    )

    def __str__(self):
        return self.operator_type

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RiskFactorsData"



class Association_Membership(models.Model):

    assocName = models.CharField(max_length=50, default="", blank=True)
    membershipNum = models.CharField(max_length=10, default="", blank=True)
    assoc_URL = models.TextField(validators=[URLValidator()])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="associations"
    )

    def __str__(self):
        return self.assocName

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Associations"


class Inspection(models.Model):
    regNum = models.CharField(max_length=14)
    op_firstName = models.CharField(max_length=32)
    op_middleName = models.CharField(max_length=50)
    op_lastName = models.CharField(max_length=50)

    soc_1 = models.BooleanField(default=False)
    soc_2 = models.BooleanField(default=False)
    soc_3 = models.BooleanField(default=False)
    soc_4 = models.BooleanField(default=False)
    soc_5 = models.BooleanField(default=False)
    soc_6 = models.BooleanField(default=False)
    soc_7 = models.BooleanField(default=False)
    soc_8 = models.BooleanField(default=False)
    soc_9 = models.BooleanField(default=False)
    soc_10 = models.BooleanField(default=False)
    soc_11 = models.BooleanField(default=False)

    soc_1_comment = models.TextField()
    soc_2_comment = models.TextField()
    soc_3_comment = models.TextField()
    soc_4_comment = models.TextField()
    soc_5_comment = models.TextField()
    soc_6_comment = models.TextField()
    soc_7_comment = models.TextField()
    soc_8_comment = models.TextField()
    soc_9_comment = models.TextField()
    soc_10_comment = models.TextField()
    soc_11_comment = models.TextField()
    soc_12_comment = models.TextField()
    soc_13_comment = models.TextField()

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (
            self.regNum,
            self.op_lastName,
            self.op_firstName,
        )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Inspections"
