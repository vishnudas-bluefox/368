from django.http import JsonResponse
# Create your views here.

def api_index(request,*args,**kwargs):
    return JsonResponse({"Message":"Hello, world!"})