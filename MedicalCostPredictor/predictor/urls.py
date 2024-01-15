# predictor/urls.py
from django.urls import path
from .views import predict_medical_cost

urlpatterns = [
    path('predict/', predict_medical_cost, name='predict_medical_cost'),
]
