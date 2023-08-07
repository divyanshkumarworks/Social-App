from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Users.models import User, Follower

import json
import jwt

@csrf_exempt
def profile_api(request):
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

		followings = Follower.objects.filter(user_from=user)
		followers = Follower.objects.filter(user_to=user)

		data = {
				"user": []
			}

		data["user"].append(
				{
					"id": user.name,
					"followings": followings.count(),
					"followers": followers.count()
				}
			)	

		return JsonResponse(data)
	else:
		return JsonResponse({'error': 'not found'}, status=404)