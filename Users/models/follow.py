from .user import User
from django.db import models
from django.utils import timezone


class Follower(models.Model):
	user_from = models.ForeignKey(User, related_name="user_from_set", on_delete=models.CASCADE)
	user_to = models.ForeignKey(User, related_name="user_to_set", on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ["-created"]
		unique_together = ('user_from', 'user_to',)

	def clean(self):
		if self.user_to == self.user_from:
			raise ValidationError('A user cannot follow itself.')

	def __str__(self):
		return f"{self.user_from.name} started following {self.user_to.name}"