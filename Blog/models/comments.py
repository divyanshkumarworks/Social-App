from django.db import models
from django.utils import timezone
from Users.models import User
from .posts import Post

class Comment(models.Model):
	text = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

	class Meta:
		ordering = ('-created',)

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f"{self.user} comment on post {self.post.id}" 	