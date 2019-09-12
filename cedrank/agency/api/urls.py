from django.urls import path
from .views import DebtorsListView, DebtorsDetailView

urlpatterns = [
    path('',DebtorsListView.as_view()),
    path('<pk>',DebtorsDetailView.as_view())

]