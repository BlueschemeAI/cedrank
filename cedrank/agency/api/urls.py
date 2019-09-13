from django.urls import path
from .views import DebtorsListView, DebtorsDetailView, CreditorsIdListView

urlpatterns = [
    path('',DebtorsListView.as_view()),
    path('<pk>',DebtorsDetailView.as_view())
    #path('cid',CreditorsIdListView.as_view()),

]