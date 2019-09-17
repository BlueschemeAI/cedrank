from django import forms
from django.forms import ModelChoiceField
from agency.models import Debtors, Creditors


class DebtorsAddForm(forms.ModelForm):
    creditors = ModelChoiceField(Creditors.objects.all(), empty_label=None)

    class Meta:
        model = Debtors
        fields = (
            'name',
            'individual_id',
            'gender',
            'age',
            'phone',
            'email',
            'Address',
            'photo',
            'debt_amount',
            'case_details',
            'document',
            'creditors'
        )


class CreditorsAddForm(forms.ModelForm):

    class Meta:
        model = Creditors
        fields = (
            'name',
            'gender',
            'age',
            'phone',
            'email',
            'Address',
            'photo'
        )


class CidFilterDebtorsForm(forms.ModelForm):
    class Meta:
        model = Creditors
        fields = ('clientid',)
