from django.views import View
from django.views.decorators.csrf import csrf_exempt
from Blog.models import Post, Comment
from Users.models import User
from django.http import JsonResponse
from django.core.serializers import serialize


import json
import jwt

@csrf_exempt
def get_all_posts_api(request):
	
	token = request.COOKIES.get('jwt_token')
	if token:	
		payload = jwt.decode(
			token,
			key="my_secret_key",
			algorithms=["HS256"]
			)
		
		email = payload["email"]
		password = payload["password"]

		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			return JsonResponse({"message": "invalid user"})

		user_id = user.id
		posts = Post.objects.filter(user=user_id)

		data = {
			"posts": []
		}

		for post in posts:
			comments = Comment.objects.filter(post=post)
			data["posts"].append(
					{
						"id": post.id,
						"title": post.title,
						"description": post.description,
						"created_at": post.created,
						"likes": post.likes.all().count(),
						"comment": [comment.text for comment in comments]
					}
				)	

		return JsonResponse(data)
	else:
		return JsonResponse({'error': 'not found'}, status=404)