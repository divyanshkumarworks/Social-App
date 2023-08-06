from django.db import models
from Users.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name="likes",blank=True)

	def __str__(self):
		return f"{self.title} created by {self.user}"

		