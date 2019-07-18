from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from core.models import Question
from core.forms import QuestionForm
from django.contrib.auth.decorators import login_required

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


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                user = request.user

            )
        question.save()
        return HttpResponseRedirect(reverse_lazy('question_detail',kwargs =
        {'pk':question.pk}))
    else:
        form = QuestionForm()
    context = {
        'form': form
    }

    return render(request, 'core/question_create.html', context)