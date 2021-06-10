from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    #database table name
    post_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=130)
    thumbnail = models.ImageField(upload_to="blogpost/images", default="")
    post_title = models.CharField(max_length=500, default=None)
    content = models.TextField(max_length=5000000, default=None)
    author = models.CharField(max_length=200, default=None)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)

    #showing sender name without pressing the message
    def __str__(self):
        return str(self.post_id) +'-'+ self.author +'--'+ self.post_title


class Blogpostcomment(models.Model):
    com_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username