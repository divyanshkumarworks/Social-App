from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import jwt

@csrf_exempt
def authenticate_user(request):
	if request.method == "POST":
		data = json.loads(request.body)

		email = data["email"]
		password = data["password"]

		payload_data = {  
			  "sub": "1",  
			  "email": email,  
			  "password": password 
			}  
			
		token = jwt.encode(
			payload=payload_data,
			key = "my_secret_key"  
			)

		response = JsonResponse({"token": token})   
		response.set_cookie("jwt_token", token)
		return response
	else:
		return JsonResponse({"mesage": "email or password not given"})