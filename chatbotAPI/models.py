from django.db import models

# Each conversation will go like:
# Human: Hi, how are you? (a queston)
# Bot: I'm fine thanks, you? (an answer)
class Conversation(models.Model):
    # The max length is based on the default model, change it to your desired number
    question = models.CharField(max_length=40)
    answer = models.CharField(max_length=40)
