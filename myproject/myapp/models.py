from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DictionaryEntry(models.Model):
    word = models.CharField(max_length=255)
    definition = models.TextField()
    origin_language = models.CharField(max_length=255)

    def __str__(self):
        return self.word

    class Meta:
        db_table = "dictionary_entry"


class UserComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    dictionary_word = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}, Comment: {self.comment}"

    class Meta:
        db_table = 'user_comments'
