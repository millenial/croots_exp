# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from favfood.models import UserLikesFood
from userinfo.models import User

def getAllInformation(request):
    foods = UserLikesFood.objects.all()
    
    results = {}
    
    for f in foods:
        results.add(User.objects.get())
    
    return render_to_response('food.html', {'results': results})