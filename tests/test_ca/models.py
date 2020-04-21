from django.db import models

from localflavor.ca.models import CAPostalCodeField, CAProvinceField, CASocialInsuranceNumberField


class CAPlace(models.Model):
    province = CAProvinceField(blank=True)
    province_req = CAProvinceField()
    province_default = CAProvinceField(default="CA", blank=True)
    name = models.CharField(max_length=20)
    ssn = CASocialInsuranceNumberField(blank=True)
    postal_code = CAPostalCodeField(blank=True)
