from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
class Photo(models.Model):
    title = models.CharField(max_length=255,blank=True)
    photo = models.FileField(upload_to='photos')
    description = models.TextField(blank=True)
    uploaded = models.DateTimeField(auto_now_add=True,blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True)

class UploadFile(models.Model):
    title = models.CharField(max_length = 50)
    file = models.FileField(upload_to='pic')