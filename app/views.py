from django.shortcuts import render
from .utils import *
from django.contrib.auth import User
from .models import *
import uuid 
from .utils import *
# Create your views here.
def app(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User(username = email)
        user_obj.set_password(password)
        p_obj = Profile.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid4())
        )
        send_email_token(email, p_obj.email_token)
    return render(request , 'home.html')



def verify(request , token):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse('invalid')


