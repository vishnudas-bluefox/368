from django.urls import path

from . import views

urlpatterns = [
    path('rtipdf/',views.createpdf),

]