import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordsApp.settings')
django.setup()

from questions.models import Sentence, Word

"""
    {
        sentences: [
            {
                text =>
                correct => 
                pos => 
                1234 5678
                p1234pptextpp5678
                words => [
                    {
                        text
                    },
                    {
                        text
                    }
                ]
            }
        ]
    }
"""

def load_data():
    with open('sample.json') as f:
        data = json.load(f)
        for ob in data["sentences"]:
            s = Sentence.objects.create(
                text=ob['text'],
                word_position=ob['pos'],
                correct_answer=ob['correct']
            )
            for word in ob["words"]:
                Word.objects.create(
                    text=word,
                    sentence=s
                )



if __name__ == '__main__':
    load_data()