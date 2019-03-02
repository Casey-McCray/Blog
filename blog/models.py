from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('comment-create', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #unrestricted size
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.post.title


