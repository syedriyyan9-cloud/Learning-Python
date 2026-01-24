from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """table schema for blog posts"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """represents object by title names"""
        return self.title
