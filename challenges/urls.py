from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:month>', views.monthly_by_num),
    path('<str:month>', views.monthly, name="month-challenge")
]