from django.urls import path
from .views import NumberPropertiesView

urlpatterns = [
    path('classify-number/', NumberPropertiesView.as_view()),
]