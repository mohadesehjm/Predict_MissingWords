from django.db import models
from django.contrib.auth import get_user_model


class Sentence(models.Model):
    text = models.CharField(max_length=1024)
    level = models.CharField(null=True,max_length=1024)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return self.text


class Blank(models.Model):
    word_position = models.PositiveIntegerField()
    correct_answer = models.CharField(max_length=256)
    sentence = models.ForeignKey(
        Sentence, on_delete=models.CASCADE, related_name='blanks'
    )



class Word(models.Model):
    text = models.CharField(max_length=256)
    blank = models.ForeignKey(
        Blank,null=True, on_delete=models.CASCADE, related_name='words'
    )


class Submission(models.Model):
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='submissions'
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='submissions'
    )
    blank = models.ForeignKey(
        Blank,null=True, on_delete=models.CASCADE, related_name='submissions'
    )