from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # logic to create a user will go here... later !!
        return JsonResponse({'message': 'Register view is working!'})
    return JsonResponse({'error' : 'POST method required.'}, status = 400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # logic to log in a user (do later cba rn!!)
        return JsonResponse({'message' : 'login view is working!'})
    return JsonResponse({'error' : 'POST method required.'}, status = 400)