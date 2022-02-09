from django.shortcuts import render, redirect
from django.views import View

from .models import Sentence, Word, Submission,Blank

class Index(View):
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        for key, value in request.POST.items():
            print("key ", key, value)
            if key.startswith('sentence-') and value.startswith('answer-'):
                blank = Blank.objects.get(
                    pk=key.split('-')[1]

                )
                # word = blank.answers.get(
                word = blank.words.get(
                    pk=value.split('-')[1]
                )
                try:
                    sub = Submission.objects.get(
                        blank=blank,
                        user=request.user
                    )
                    sub.word = word
                    sub.save()
                except Submission.DoesNotExist:
                    Submission.objects.create(
                        word=word,
                        blank=blank,
                        user=request.user
                    )
        return redirect('index')

    def get(self, request):

        if not request.user.is_authenticated:
            return redirect('login')
        level = request.GET.get('level')
        # ?level=intermediate
        if level:
            sentences = Sentence.objects.filter(level=level).order_by(
                '-created_at'
            )
        else:
            sentences = Sentence.objects.all().order_by(
                '-created_at'
            )
        sentences_ctx = []

        for sent in sentences:
            current_pos = 0
            blank_data = []
            for blank in sent.blanks.all():
                sub = Submission.objects.filter(
                    user=request.user,
                    blank = blank
                ).first()

                blank_data.append({
                    'id': blank.id,
                    'half': sent.text[current_pos:blank.word_position],
                    'choices': [{
                        'id': word.id,
                        'word': word.text
                    } for word in blank.words.all()],
                    'answer': sub,
                    'is_correct': sub.word.text == blank.correct_answer if sub else None
                })
                current_pos = blank.word_position

            sentences_ctx.append({
                "id" : sent.id,
                "blanks":blank_data,
                "last_half":sent.text[current_pos:]
            })
        return render(
            request, 'questions/index.html', {
                'sentences': sentences_ctx
            } 
        )
        