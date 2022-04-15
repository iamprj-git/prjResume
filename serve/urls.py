from django.urls import path
from serve import views

urlpatterns = [
    path('services1/',views.service,name="services"),
]