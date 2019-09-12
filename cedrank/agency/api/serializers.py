from rest_framework import serializers
#from rest_framework import Debtors
from agency.models import Debtors

class DebtorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Debtors
        fields = ('name','individual_id','gender','age','phone','email','Address','photo','debt_amount','case_details','document')
