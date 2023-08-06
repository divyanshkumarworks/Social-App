from django.http import JsonResponse
from Blog.models import Post
from Users.models import User
from django.views.decorators.csrf import csrf_exempt

import json
import jwt

@csrf_exempt
def like_post_api(request, post_id):
	if request.method == "POST":

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
			
			post = Post.objects.get(id=post_id)
			post.likes.add(user)
			return JsonResponse({"liked": True})
		else:
			return JsonResponse({"message": "invalid user"})
	else:
		return JsonResponse({'error': 'not found'}, status=404)
