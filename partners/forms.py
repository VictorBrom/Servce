from django import forms
from partners.models import Partners, Contracts, Service

class PartnersForms(forms.ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'

class ContractsForms(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'