from django import forms
from agency.models import Debtors, Creditors

class CreditorsAddForm(forms.ModelForm):
    class Meta:
        model=Creditors
        fields = ('name','clientid','gender','age','phone','email','Address','photo')

class DebtorsAddForm(forms.ModelForm):
    class Meta:
        model=Debtors
        fields = ('clientid','name','individual_id','gender','age','phone','email','Address','photo','debt_amount','case_details','document')

class CidFilterDebtorsForm(forms.ModelForm):
    class Meta:
        model=Creditors
        fields = ('clientid',)