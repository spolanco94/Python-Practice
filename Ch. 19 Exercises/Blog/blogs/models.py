from django.db import models
from django.db.models.fields import DateTimeField

class BlogPost(models.Model):
    """Model for blog post for webapp."""
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.text[:150]}..."
        