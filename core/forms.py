from django import forms

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=250)
    body = forms.CharField(max_length=250)



class AnswerForm(forms.Form):
    body = forms.CharField(max_length=250)


#class DeleteForm(forms.Form):
    #body = forms.CharField(max_length=250)

