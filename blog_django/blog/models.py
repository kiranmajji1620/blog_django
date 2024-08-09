from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# The best thing about django is orm(object relational mapping) which allow us to write the data as classes irrespective of the database we are using. This way when we want to use a different database, we don't need to change the queries as we use python instead of sql and we only need to change the settings.
# In this project, we are using sql lite for development and postgresql for production


class Post(models.Model):
    title = models.CharField(max_length = 100) # the server stores a max length
    content = models.TextField() # no limit for length of content
    date_posted = models.DateTimeField(default = timezone.now)
    # with auto_now_add set to True we can't update the date_posted
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "posts")# if the user is deleted, delete his posts.
    
    def __str__(self):
        return self.title
    
'''
Why migrations are useful:
When we want to update the database which was already created, we would have to write some complex sql queries which is hard
Having migrations, allows us to just modify the modles.py and make migrations and it will do all changes.
'''