from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    """       """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    questionstars = models.ManyToManyField(User, through='QuestionStar', related_name="questionstars")

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])

    def __str__(self):
        """    """
        return self.title

    def to_dict(self):
        return {
            'body': self.body,
            'title': self.title
        }

class Answer(models.Model):
    """      """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    answerstars = models.ManyToManyField(User, through='AnswerStar', related_name="answerstars")

    def __str__(self):
        """   """
        return self.body

    def to_dict(self):
        return {
            'body': self.body,
            'correct': self.correct
        }

class QuestionStar(models.Model):
    """  """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class AnswerStar(models.Model):
    """  """
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


