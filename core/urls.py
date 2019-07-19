from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:pk>', views.question_detail, name='question_detail'),
    path('questions/create', views.question_create, name="question_create"),
    path('questions/<int:pk>/answers/create', views.answer_create, name="answer_create"),
    path('answers/<int:pk>/mark-correct', views.answer_correct, name="answer_correct"),
    path('answers/<int:pk>/star', views.answer_star, name="answer_star"),
    path('questions/<int:pk>/star', views.question_star, name="question_star"),
]