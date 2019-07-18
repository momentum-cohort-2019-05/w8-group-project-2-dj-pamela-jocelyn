from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:pk>', views.question_detail, name='question_detail'),
    path('questions/create', views.question_create, name="question_create"),
]