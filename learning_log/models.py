from django.urls import reverse
# import uuid
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Topic(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4) 
    topic = models.CharField(max_length=30)
    datetime_add = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("topic_detail", args=[str(self.id)])
    


class Entry(models.Model):
    topics = models.ForeignKey(Topic, related_name="entry", on_delete=models.CASCADE)
    entry = models.TextField()
    datetime_add = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= 'Entries'
    
    def __str__(self) -> str:
        return self.entry
    
    # def get_absolute_url(self):
    #     return reverse("topic_detail",args=[str(self.id)] )
