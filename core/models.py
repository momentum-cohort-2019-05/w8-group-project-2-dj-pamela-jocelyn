from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    """       """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])

    def __str__(self):
        """    """
        return self.title

class Answer(models.Model):
    """      """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        """   """
        return self.body

        

