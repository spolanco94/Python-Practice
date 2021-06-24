from django.db import models
from django.db.models.fields import DateTimeField

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return string representation of the model."""        
        return self.text

class Entry(models.Model):
    """An entry specific to a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        if(len(self.text) > 50):
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"