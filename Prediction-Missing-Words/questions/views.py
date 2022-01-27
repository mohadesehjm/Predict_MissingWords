from django.shortcuts import render, redirect
from django.views import View

from .models import Sentence, Word, Submission

class Index(View):
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        for key, value in request.POST.items():
            if key.startswith('sentence-') and value.startswith('answer-'):
                sentence = Sentence.objects.get(
                    pk=key.split('-')[1]
                )
                word = sentence.answers.get(
                    pk=value.split('-')[1]
                )
                try:
                    sub = Submission.objects.get(
                        sentence=sentence,
                        user=request.user
                    )
                    sub.word = word
                    sub.save()
                except Submission.DoesNotExist:
                    Submission.objects.create(
                        word=word,
                        sentence=sentence,
                        user=request.user
                    )
        return redirect('index')

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        sentences = Sentence.objects.all().order_by(
            '-created_at'
        )
        sentences_ctx = []

        for sent in sentences:
            sub = Submission.objects.filter(
                user=request.user,
                sentence=sent
            ).first()
            sentences_ctx.append({
                'id': sent.id,
                'first_half': sent.text[:sent.word_position],
                'choices': [{
                    'id': ans.id,
                    'word': ans.text
                } for ans in sent.answers.all()],
                'second_half': sent.text[sent.word_position:],
                'answer': sub,
                'is_correct': sub.word.text == sent.correct_answer if sub else None 
            })
        return render(
            request, 'questions/index.html', {
                'sentences': sentences_ctx
            } 
        )
        