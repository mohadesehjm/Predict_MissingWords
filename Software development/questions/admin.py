from django.contrib import admin

from .models import Sentence, Word, Submission,Blank

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    pass
@admin.register(Blank)
class BlankAdmin(admin.ModelAdmin):
    pass
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass