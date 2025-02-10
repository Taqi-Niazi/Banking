from django.urls import path
from . import views

urlpatterns = [
    path("", views.banking_dashboard, name="banking_home"),
    path("balance/", views.check_balance, name="check_balance"),
    path("deposit/", views.deposit, name="deposit"),
    path("withdraw/", views.withdraw, name="withdraw"),
]
