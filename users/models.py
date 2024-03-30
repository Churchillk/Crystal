from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Jobs(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    due = models.DateTimeField()
    worth = models.CharField(max_length = 50, default="$00.00")
    cartegory = models.CharField(max_length = 50, default = "coding")
    status = models.BooleanField(default = False)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # action 
    
    def __str__(self):
        return f'{self.author} profile'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = [ 'status' ]
    
    
