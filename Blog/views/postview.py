from django.views import View
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from Blog.models import Post
from Users.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.core.serializers import serialize

import json
import jwt

@method_decorator(csrf_exempt, name='dispatch')
class PostView(View):

	def get(self, request, post_id):

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
			post = Post.objects.get(id=post_id)

			data = {
				"post": []
			}

			data["post"].append(
					{
						"id": post.id,
						"title": post.title,
						"description": post.description,
						"created_at": post.created,
						"likes": post.likes.all().count()
					}
				)	

			return JsonResponse(data)
		else:
			return JsonResponse({'error': 'not found'}, status=404)


	def post(self, request):

		data = json.loads(request.body)

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
			
			title = data["title"]
			description = data["description"]

			try:
				with transaction.atomic():
					post = Post(user=user, title=title, description=description)
					post.save()
			except Exception as e:
				return JsonResponse({"message": str(e)})

			return JsonResponse({"message":"success"})
		else:
			return JsonResponse({'error': error.message}, status=404)

	def delete(self, request, post_id):
		
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

			post = Post.objects.filter(id=post_id)
			post.delete()

			return JsonResponse({"message": "task deleted"})

		# else:
		# 	return JsonResponse({'error': 'not found'}, status=404)

