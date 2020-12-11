from django.db import models

# Create your models here.


class Exam(models.Model):

    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.question

    class Meta:
        db_table="howdy_exam"


class ShortExam(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

