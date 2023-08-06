from django.http import JsonResponse
from Blog.models import Post, Comment
from Users.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

import json
import jwt

@csrf_exempt
def comment_on_post(request, post_id):
	if request.method == "POST":
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

			comment = data["comment"]
			post = Post.objects.get(id=post_id)

			try:
				with transaction.atomic():
					comment = Comment(text=comment, user=user, post=post)
					comment.save()
			except Exception as e:
				return JsonResponse({"message": str(e)})

			return JsonResponse({"message":"success"})
		else:
			return JsonResponse({'error': error.message}, status=404)