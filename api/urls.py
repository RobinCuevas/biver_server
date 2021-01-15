from django.urls import path
from .views import InvoicesRestaurant

urlpatterns = [
    path('invoices/', InvoicesRestaurant.as_view()),
]