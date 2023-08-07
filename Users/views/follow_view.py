from django.http import JsonResponse
from Users.models import Follower, User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

import json
import jwt

@csrf_exempt
def follow_api(request, user_id):
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

			followed = get_object_or_404(User, id=user_id)
			followed_by = user



			if followed_by.id == followed.id:
				return JsonResponse({"message": "user cannot follow itself"})

			Follower.objects.create(user_to=followed,user_from=followed_by)

			return JsonResponse({"message": f"user {followed_by.id} is following user {followed.id}"})
	else:
		return JsonResponse({'error': 'not found'}, status=404)







