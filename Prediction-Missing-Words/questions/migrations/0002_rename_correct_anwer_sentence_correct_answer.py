# Generated by Django 4.0.1 on 2022-01-16 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentence',
            old_name='correct_anwer',
            new_name='correct_answer',
        ),
    ]