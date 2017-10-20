from django.contrib.gis.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return str(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class MapImage(models.Model):
    name = models.CharField('Name', max_length=100)
    image = models.ImageField(upload_to = 'images', null=True, blank=True)
    location = models.PointField(blank=False, null=False)

    def __str__(self):
        return self.name
