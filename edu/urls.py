from django.urls import path
from edu import views
urlpatterns = [
    path('edu/',views.qualif,name="edu")
]
