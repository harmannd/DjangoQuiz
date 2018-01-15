from django.db import models

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50)
    #difficulty
    #completions

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    #correctly answered count

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str__(self):
        return self.answer_text