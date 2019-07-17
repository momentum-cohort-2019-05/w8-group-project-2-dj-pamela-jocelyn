from django.shortcuts import render
from core.models import Question

# Create your views here.

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': questions
    }

    return render(request, 'index.html', context)

def question_detail(request, pk):
    question = Question.objects.get(pk=pk)

    context = {
        'question': question
    }

    return render(request, 'core/question_detail.html', context)


