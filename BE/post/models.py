from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()             # content 컬럼
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title