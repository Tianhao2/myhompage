from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>/', views.survey_form, name='survey_form'),
    path('<str:category>/thankyou/', views.survey_thankyou, name='survey_thankyou'),
]
