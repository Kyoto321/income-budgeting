from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpensesList.as_view(), name="expenses"),
    path('<int:id>/', views.ExpensesDetailView.as_view(), name="expense"),
]
