from django.db import models
from django.contrib.auth import get_user_model

class Sentence(models.Model):
    text = models.CharField(max_length=1024)
    word_position = models.PositiveIntegerField()
    # New  sentence.
    correct_answer = models.CharField(max_length=256)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return self.text[:self.word_position] + '*****' \
            + self.text[self.word_position:] \
            + ' AN: ' + self.correct_answer

class Word(models.Model):
    text = models.CharField(max_length=256)
    sentence = models.ForeignKey(
        Sentence, on_delete=models.CASCADE, related_name='answers'
    )

    def __str__(self, ):
        return 'WORD: ' + self.text + ' FOR: ' + str(self.sentence)

class Submission(models.Model):
    sentence = models.ForeignKey(
        Sentence, on_delete=models.CASCADE, related_name='submissions'
    )
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='submissions'
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='submissions'
    )