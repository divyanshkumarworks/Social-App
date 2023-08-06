# from .user import User

# class UserFollowing(models.Model):
# 	user_from = models.ForeignKey(User, related_name="user_from_set", on_delete=models.CASCADE)
# 	user_to = models.ForeignKey(User, related_name="user_to_set", on_delete=models.CASCADE)
# 	created = models.DateTimeField(default=timezone.now)

# 	class Meta:
# 		ordering = ["-created"]
# 		unique_together = ('user_from', 'user_to',)

# 	def __str__(self):
# 		return f"{self.user_from.username} started following {self.user_to.username}"