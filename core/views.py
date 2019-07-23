from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from core.models import Question, Answer, QuestionStar, AnswerStar
from core.forms import QuestionForm, AnswerForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
import json

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


@login_required
def answer_create(request, pk):
    question = Question.objects.get(pk=pk)
    req_data = json.loads(request.body.decode("UTF-8"))
    answer = Answer (
        question = question,   
        body = req_data['body'],
        user = request.user)
    answer.save()
    return JsonResponse({
        "body": req_data['body'],
        "user": answer.user.username
    })
      

# @login_required
# def answer_create(request, pk):
#     question = Question.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = Answer (
#                 question = question,   
#                 body = form.cleaned_data['body'],
#                 user = request.user)
#             answer.save()
#             return HttpResponseRedirect(reverse_lazy('question_detail',kwargs ={'pk':question.pk}))
#     else:
#         form = AnswerForm()
#     context = {
#         'form': form
#     }

#     return render(request, 'core/answer_create.html', context)


def answer_correct(request, pk):
    answer = Answer.objects.get(pk=pk)

    if request.user == answer.question.user:
        answer.correct = True
        answer.save()

        return JsonResponse(answer.to_dict())

def answer_star(request, pk):
        answer = Answer.objects.get(pk=pk)
        answer.answerstars.add(request.user)

        return JsonResponse(answer.to_dict())

def question_star(request, pk):
        question = Question.objects.get(pk=pk)
        question.questionstars.add(request.user)

        return JsonResponse(question.to_dict())

@login_required
def user_profile(request):
        questionstars = QuestionStar.objects.filter(user=request.user)
        answerstars = AnswerStar.objects.filter(user=request.user)
        questions = Question.objects.filter(user=request.user)
        context = {
            'questionstars': questionstars,
            'answerstars': answerstars,
            'questions': questions,
            
            
        }
        return render(request, 'core/user_profile.html', context)

class QuestionDelete(DeleteView):
    model = Question
    success_url =reverse_lazy('my_profile')
    



     
    




