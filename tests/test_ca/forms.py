from django.forms import ModelForm

from .models import CAPlace


class CAPlaceForm(ModelForm):

    class Meta:
        model = CAPlace
        fields = ('province', 'province_req', 'province_default', 'name', 'ssn', 'postal_code')
