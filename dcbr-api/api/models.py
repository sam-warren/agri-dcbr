from django.db import models
import datetime
from django.core.validators import URLValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _



class RegistrationNumber(models.Model):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    CANCELLED = "CANCELLED"
    PENDING_PAYMENT = "PENDING_PAYMENT"
    PENDING_INSPECTOR_REVIEW = "PENDING_INSPECTOR_REVIEW"
    PENDING_RENEWAL = "PENDING_RENEWAL"

    REG_STATUS_CHOICES = (
        (ACTIVE, "ACTIVE"),
        (SUSPENDED, "SUSPENDED"),
        (CANCELLED, "CANCELLED"),
        (PENDING_PAYMENT, "PENDING_PAYMENT"),
        (PENDING_INSPECTOR_REVIEW, "PENDING_INSPECTOR_REVIEW"),
        (PENDING_RENEWAL, "PENDING_RENEWAL"),
    )

    operator_status = models.CharField(
        max_length=50, choices=REG_STATUS_CHOICES, default=ACTIVE
    )

    def __str__(self):
        return "BC-DCBR-" + str(self.pk).zfill(6)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RegistrationNumbers"
        verbose_name = "new registration"


class Operator(models.Model):

    EMAIL = "Email"
    MAIL = "Mail"

    BREEDER = "BREEDER"
    SELLER = "SELLER"
    BOTH = "BREEDER&SELLER"
    OPERATION_TYPE_CHOICES = (
        (BREEDER, "BREEDER"),
        (SELLER, "SELLER"),
        (BOTH, "BREEDER&SELLER"),
    )

    description = _("An operator is a seller/breeder of cats and/or dogs")
    registrationNumber = models.OneToOneField(
        RegistrationNumber,
        on_delete=models.CASCADE,
        related_name="operator",
        related_query_name="operators",
    )
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=12, default="", blank=True)
    email_address = models.CharField(max_length=32, default="", blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    CONTACT_METHOD_CHOICE = ((EMAIL, "email"), (MAIL, "mail"))
    comm_pref = models.CharField(
        "Communication method",
        max_length=10,
        choices=CONTACT_METHOD_CHOICE,
        default=EMAIL,
    )
    operation_type = models.CharField(
        max_length=20, choices=OPERATION_TYPE_CHOICES, default=BREEDER
    )

    operation_name = models.CharField(max_length=32, default="", blank=True)
    operation_URL = models.CharField(max_length=4000, default="", blank=True)

    

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (self.registrationNumber, self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

    class Meta:
        verbose_name_plural = "Operators"
        verbose_name = "Operators : breeders and sellers"


class Address(models.Model):
    PRIMARY = "PRI"
    OPERATION = "OPN"
    TYPE_CHOICES = ((PRIMARY, "Primary"), (OPERATION, "Operation"))
    registrationNumber = models.ForeignKey(
        RegistrationNumber,
        on_delete=models.CASCADE,
        related_name="addresses",
        related_query_name="addresses",
    )
    address_type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=PRIMARY)
    street_num = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    suite = models.CharField(max_length=32, default="", blank=True)
    street_name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=7)
    province = models.CharField(max_length=2, default="BC")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (self.registrationNumber, self.type, self.street_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"


class Risk_Factor_Operation(models.Model):

    TATTOO = "TATTOO"
    MICROCHIP = "MICROCHIP"
    OTHER = "OTHER"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    PERMANENT_ID_CHOICES = (
        (TATTOO, "TATTOO"),
        (MICROCHIP, "MICROCHIP"),
        (OTHER, "OTHER"),
        (NOT_APPLICABLE, "NOT_APPLICABLE"),
    )

    DOG = "DOG"
    CAT = "CAT"
    BOTH = "DOG&CAT"

    ANIMAL_TYPE_CHOICES = ((DOG, "DOG"), (CAT, "CAT"), (BOTH, "DOG&CAT"))
    registrationNumber = models.ForeignKey(
        RegistrationNumber,
        on_delete=models.CASCADE,
        related_name="risk_factor_operations",
        related_query_name="risk_factor_operations",
    )

    accidental_breeding = models.BooleanField(default=False)
    num_workers = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    animal_type = models.CharField(
        max_length=10, choices=ANIMAL_TYPE_CHOICES, default=BOTH
    )
    num_breeds_dogs = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_breeds_cats = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    has_vet = models.BooleanField(default=False)
    has_perm_id = models.BooleanField(default=False)
    perm_id_type = models.CharField(
        max_length=15, choices=PERMANENT_ID_CHOICES, default=NOT_APPLICABLE
    )
    perm_id_other = models.CharField(max_length=15, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return "Operation risk for: \t %s " % (self.registrationNumber)
        return "Reg ID: \t %s %s" % (self.registrationNumber, self.animal_type)

    def publish(self):
        "operator = breeder / seller"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RiskFactorOperations"


class Risk_Factor_Animal(models.Model):

    registrationNumber = models.ForeignKey(
        RegistrationNumber,
        on_delete=models.CASCADE,
        related_name="risk_factor_animals",
        related_query_name="risk_factor_animals",
    )

    num_dogs_intact = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_litter_whelped = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_cats_intact = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_litter_queened = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_dog_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_dog_transferred = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_dog_traded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_dog_leased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_transferred = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_cat_traded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_leased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return "Reg ID:: \t %s " % (self.registrationNumber)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RiskFactorAnimals"


class Association_Membership(models.Model):

    registrationNumber = models.ForeignKey(
        RegistrationNumber, on_delete=models.CASCADE, related_name="associations"
    )

    assoc_name = models.CharField(max_length=50, default="", blank=True)
    membership_num = models.CharField(max_length=10, default="", blank=True)
    assoc_URL = models.CharField(max_length=50, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reg ID:: \t %s " % (self.registrationNumber)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Associations"


class Inspection(models.Model):
    registrationNumber = models.ForeignKey(
        RegistrationNumber,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="inspections",
    )
   
    op_first_name = models.CharField(max_length=32)
    op_middle_name = models.CharField(max_length=50)
    op_last_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    soc_1 = models.BooleanField(default=False)
    # soc_1_comment = models.TextField(default="", blank=True)
    soc_1_comment = models.CharField(max_length=4000, default="", blank=True)
    soc_2 = models.BooleanField(default=False)
    soc_2_comment = models.TextField(default="", blank=True)
    soc_3 = models.BooleanField(default=False)
    soc_3_comment = models.TextField(default="", blank=True)
    soc_4 = models.BooleanField(default=False)
    soc_4_comment = models.TextField(default="", blank=True)
    soc_5 = models.BooleanField(default=False)
    soc_5_comment = models.TextField(default="", blank=True)
    soc_6 = models.BooleanField(default=False)
    soc_6_comment = models.TextField(default="", blank=True)
    soc_7 = models.BooleanField(default=False)
    soc_7_comment = models.TextField(default="", blank=True)
    soc_8 = models.BooleanField(default=False)
    soc_8_comment = models.TextField(default="", blank=True)
    soc_9 = models.BooleanField(default=False)
    soc_9_comment = models.TextField(default="", blank=True)
    soc_10 = models.BooleanField(default=False)
    soc_10_comment = models.TextField(default="", blank=True)
    soc_11 = models.BooleanField(default=False)
    soc_11_comment = models.TextField(default="", blank=True)

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (
            self.registrationNumber,
            self.op_last_name,
            self.op_first_name,
        )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Inspections"
