from django.db import models


class Topic(models.Model):
    """Topic applied by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returning text model representation"""
        return self.text


class Entry(models.Model):
    """Progress of learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returning text model representation"""
        if len(self.text) > 50:
            return f"{self.text[:50]} ..."
        else:
            return self.text

