from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    """       """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    def __str__(self):
        """    """
        return self.body

class Answer(models.Model):
    """      """
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        """   """
        return self.body

        

