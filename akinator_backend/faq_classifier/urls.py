from django.urls import path
from .views import classify_query

urlpatterns = [
    path('predict/', classify_query, name='predict_query'),
]

