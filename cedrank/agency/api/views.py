from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import DebtorsSerializer
from agency.models import Debtors, Creditors

class DebtorsListView(ListAPIView):
    queryset=Debtors.objects.all()
    serializer_class=DebtorsSerializer

class DebtorsDetailView(RetrieveAPIView):
    queryset=Debtors.objects.all()
    serializer_class=DebtorsSerializer



