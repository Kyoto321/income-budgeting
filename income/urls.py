from django.urls import path
from . import views

urlpatterns = [
    path('', views.IncomeList.as_view(), name="incomes"),
    path('<int:id>/', views.IncomeDetailView.as_view(), name="income"),
]
