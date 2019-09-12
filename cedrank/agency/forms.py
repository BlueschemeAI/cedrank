from django import forms
from agency.models import Debtors, Creditors

class DebtorsAddForm(forms.ModelForm):
    class Meta:
        model=Debtors
        fields = ('name','individual_id','gender','age','phone','email','Address','photo','debt_amount','case_details','document')

class CreditorsAddForm(forms.ModelForm):
    class Meta:
        model=Creditors
        fields = ('name','individual_id','gender','age','phone','email','Address','photo')
