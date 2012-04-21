# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from favfood.models import UserLikesFood
from userinfo.models import User

def getAllInformation(request):
    foods = UserLikesFood.objects.all()
    
    results = {}
    users = User.objects.all()
    for x in users:
        myfood = UserLikesFood.objects.get(userid__id = x.id)
        results[x.username] = myfood.favoriteFood
    
    return render_to_response('food.html', {'results': results})