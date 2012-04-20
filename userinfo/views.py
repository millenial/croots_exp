# Create your views here.
from django.http import HttpResponse
from userinfo.models import User

def main(request):
    output = ', '.join([usr.username for usr in User.objects.all()])
    return HttpResponse("User details : "+output)