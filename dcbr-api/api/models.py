import logging
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

LOGGER = logging.getLogger(__name__)


class Registration(models.Model):
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

    registration_number = models.CharField(max_length=20, default="", blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.registration_number:
            self.registration_number = "BC-DCBR-" + str(self.pk).zfill(6)
            LOGGER.debug(
                "Registration_number is blank.  Saving the value as: {}".format(
                    self.registration_number
                )
            )
            self.save()
        else:
            LOGGER.debug(
                "Registration_number={}".format(
                    self.registration_number
                )
            )

    class Meta:
        verbose_name_plural = "Registrations"
        verbose_name = "new registration"


class Operator(models.Model):

    EMAIL = "Email"
    MAIL = "Mail"
    PHONE = "Phone"
    CONTACT_METHOD_CHOICE = ((EMAIL, "Email"), (MAIL, "Mail"), (PHONE, "Phone"))

    BREEDER = "BREEDER"
    SELLER = "SELLER"
    BOTH = "BREEDER&SELLER"
    OPERATION_TYPE_CHOICES = (
        (BREEDER, "BREEDER"),
        (SELLER, "SELLER"),
        (BOTH, "BREEDER&SELLER"),
    )

    description = _("An operator is a seller/breeder of cats and/or dogs")
    registration_number = models.OneToOneField(
        Registration,
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
        return "Reg ID: \t %s %s , %s" % (
            self.registration_number,
            self.last_name,
            self.first_name,
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Operators"
        verbose_name = "Operators : breeders and sellers"


class Address(models.Model):
    MAILING = "MAIL"
    OPERATION = "OPN"
    TYPE_CHOICES = ((MAILING, "Mailing"), (OPERATION, "Operation"))

    # List of regions
    ALBERNI_CLAYOQUOT = "Alberni-Clayoquot"
    BULKLEY_NECHAKO = "Bulkley-Nechako"
    CAPITAL = "Capital"
    CARIBOO = "Cariboo"
    CENTRAL_COAST = "Central Coast"
    CENTRAL_KOOTENAY = "Central Kootenay"
    CENTRAL_OKANAGAN = "Central Okanagan"
    COLUMBIA_SHUSWAP = "Columnbia Shuswap"
    COMOX_VALLEY = "Comox Valley"
    COWICHAN_VALLEY = "Cowichan Valley"
    EAST_KOOTENAY = "East Kootenay"
    FRASER_VALLEY = "Fraser Valley"
    FRASER_FORT_GEORGE = "Fraser-Fort George"
    ISLANDS_TRUST = "Islands Trust"
    KITIMAT_STIKINE = "Kitimat Stikine"
    KOOTENAY_BOUNDARY = "Kootenay Boundary"
    METRO_VANCOUVER = "Metro Vancouver"
    MOUNT_WADDINGTON = "Mount Waddington"
    NANAIMO = "Nanaimo"
    NORTH_OKANAGAN = "North Okanagan"
    NORTH_COAST = "North Coast"
    OKANAGAN_SIMILKAMEEN = "Okanagan-Similkameen"
    PEACE_RIVER = "Peace River"
    GATHET = "Gathet"
    SQUAMISH_LILLOOET = "Squamish-Lillooet"
    STRATHCONA = "Strathcona"
    SUNSHINE_COAST = "Sunshine Coast"
    THOMPSON_NICOLA = "Thompson-Nicola"

    TYPE_CHOICES = ((MAILING, "Mailing"), (OPERATION, "Operation"))
    REGIONAL_CHOICES = (
        (ALBERNI_CLAYOQUOT, "Alberni-Clayoquot"),
        (BULKLEY_NECHAKO, "Buckley-Nechako"),
        (CAPITAL, "Capital"),
        (CARIBOO, "Cariboo"),
        (CENTRAL_COAST, "Central Coast"),
        (CENTRAL_KOOTENAY, "Central Kootenay"),
        (CENTRAL_OKANAGAN, "Central Okanagan"),
        (COLUMBIA_SHUSWAP, "Columbia Shuswap"),
        (COMOX_VALLEY, "Comox Valley"),
        (COWICHAN_VALLEY, "Cowichan Valley"),
        (EAST_KOOTENAY, "East Kootenay"),
        (FRASER_VALLEY, "Fraser Valley"),
        (FRASER_FORT_GEORGE, "Fraser-Fort George"),
        (ISLANDS_TRUST, "Islands Trust"),
        (KITIMAT_STIKINE, "Kitimat-Stikine"),
        (KOOTENAY_BOUNDARY, "Kootenay-Boundary"),
        (METRO_VANCOUVER, "Metro Vancouver"),
        (MOUNT_WADDINGTON, "Mount Waddington"),
        (NANAIMO, "Nanaimo"),
        (NORTH_OKANAGAN, "North Okanagan"),
        (NORTH_COAST, "North Coast"),
        (OKANAGAN_SIMILKAMEEN, "Okanagan-Similkameen"),
        (PEACE_RIVER, "Peace River"),
        (GATHET, "qathet"),
        (SQUAMISH_LILLOOET, "Squamish-Lillooet"),
        (STRATHCONA, "Strathcona"),
        (SUNSHINE_COAST, "Sunshine Coast"),
        (THOMPSON_NICOLA, "Thompson-Nicola"),
    )

    registration_number = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name="addresses",
        related_query_name="addresses",
    )
    address_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default=MAILING)
    street_num = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    suite = models.CharField(max_length=32, default="", blank=True)
    street_name = models.CharField(max_length=32)
    POBox = models.CharField(max_length=32, default="", blank=True)
    city = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=7)
    province = models.CharField(max_length=2, default="BC")
    region = models.CharField(max_length=20, choices=REGIONAL_CHOICES, default="")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (
            self.registration_number,
            self.address_type,
            self.street_name,
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"


class Operation_Risk_Factor(models.Model):

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

    registration_number = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name="operation_risk_factors",
        related_query_name="operation_risk_factors",
    )

    accidental_breeding = models.BooleanField(default=False)
    num_workers = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    has_vet = models.BooleanField(default=False)
    has_perm_id = models.BooleanField(default=False)
    perm_id_type = models.CharField(
        max_length=15, choices=PERMANENT_ID_CHOICES, default=NOT_APPLICABLE
    )
    perm_id_other = models.CharField(max_length=15, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Operation risk for: \t %s " % (self.registration_number)
        return "Reg ID: \t %s %s" % (self.registration_number, self.animal_type)

    def publish(self):
        "operator = breeder / seller"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Operation_Risk_Factors"


class Animal_Risk_Factor(models.Model):

    registration_number = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name="animal_risk_factors",
        related_query_name="animals_risk_factors",
    )

    DOG = "DOG"
    CAT = "CAT"
    BOTH = "DOG&CAT"

    ANIMAL_TYPE_CHOICES = ((DOG, "DOG"), (CAT, "CAT"))

    animal_type = models.CharField(
        max_length=10, choices=ANIMAL_TYPE_CHOICES, default=DOG
    )
    num_breeds = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    num_females_intact = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_litter = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    num_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_transferred = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_traded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_leased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_animals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reg ID:: \t %s " % (self.registration_number)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Animal_Risk_Factors"


class Association_Membership(models.Model):

    registration_number = models.ForeignKey(
        Registration, on_delete=models.CASCADE, related_name="associations"
    )

    assoc_name = models.CharField(max_length=50, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reg ID:: \t %s " % (self.registration_number)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Associations"


class Renewal(models.Model):

    # this model is a temporary fix to allow operators to re-register, without authentication
    # In the front-end, an operator that renews their registration is expected to enter some 
    # information from their previous registration.
    # **************** Please do not count on this information being accurate **************

    registration_number = models.ForeignKey(
        Registration, on_delete=models.CASCADE, related_name="renewals"
    )

    first_name = models.CharField(max_length=32, default="", blank=True)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    previous_registration_number = models.CharField(
        max_length=20, default="", blank=True
    )
    # Note - expiry date is simply a self-reported expiry date
    expiry_date = models.CharField(max_length=10, default= "", blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reg ID:: \t %s " % (self.registration_number)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Renewals"


class Inspection_Report(models.Model):
    registration_number = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="inspections",
    )
    inspector_full_name = models.CharField(max_length=50, default="")
    operator_first_name = models.CharField(max_length=32)
    operator_middle_name = models.CharField(max_length=50, default="", blank=True)
    operator_last_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    Record_Keeping = models.BooleanField(default=False)
    Record_Keeping_notes = models.TextField(default="", blank=True)

    Required_Plans = models.BooleanField(default=False)
    Required_Plans_notes = models.TextField(default="", blank=True)

    Environment = models.BooleanField(default=False)
    Environment_notes = models.TextField(default="", blank=True)

    Protection_from_Injury_and_Illness = models.BooleanField(default=False)
    Protection_from_Injury_and_Illness_notes = models.TextField(default="", blank=True)

    Containment = models.BooleanField(default=False)
    Containment_notes = models.TextField(default="", blank=True)

    Tethering = models.BooleanField(default=False)
    Tethering_notes = models.TextField(default="", blank=True)

    Transportation = models.BooleanField(default=False)
    Transportation_notes = models.TextField(default="", blank=True)

    Food_and_Water = models.BooleanField(default=False)
    Food_and_Water_notes = models.TextField(default="", blank=True)

    Handling = models.BooleanField(default=False)
    Handling_notes = models.TextField(default="", blank=True)

    Grooming_and_Nail_Care = models.BooleanField(default=False)
    Grooming_and_Nail_Care_notes = models.TextField(default="", blank=True)

    Socialization_and_Exercise = models.BooleanField(default=False)
    Socialization_and_Exercise_notes = models.TextField(default="", blank=True)

    Health_Care = models.BooleanField(default=False)
    Health_Care_notes = models.TextField(default="", blank=True)

    Breeding = models.BooleanField(default=False)
    Breeding_notes = models.TextField(default="", blank=True)

    Queening_and_Whelping = models.BooleanField(default=False)
    Queening_and_Whelping_notes = models.TextField(default="", blank=True)

    Veterinary_Care = models.BooleanField(default=False)
    Veterinary_Care_notes = models.TextField(default="", blank=True)

    Exercise = models.BooleanField(default=False)
    Exercise_notes = models.TextField(default="", blank=True)

    Handling_and_Training = models.BooleanField(default=False)
    Handling_and_Training_notes = models.TextField(default="", blank=True)

    Euthanasia = models.BooleanField(default=False)
    Euthanasia_notes = models.TextField(default="", blank=True)

    def __str__(self):
        return "Reg ID: \t %s Name: \t %s , %s" % (
            self.registration_number,
            self.operator_last_name,
            self.operator_first_name,
        )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Inspections"
