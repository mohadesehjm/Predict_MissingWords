import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordsApp.settings')
django.setup()

from questions.models import Sentence, Word, Blank


def load_data():
    with open('input.json') as f:
        data = json.load(f)
        for ob in data["sentences"]:
            s = Sentence.objects.create(
                text = ob['text'],
                level = ob['level'],
            )
            for blank in ob['blank']:
                b = Blank.objects.create(
                    correct_answer= blank['correct'],
                    word_position= blank['pos'],
                    sentence = s
                )
                for word in blank["words"]:
                    Word.objects.create(
                        text=word,
                        blank = b
                    )


if __name__ == '__main__':
    load_data()