from django.shortcuts import render
import social_django.models as sm
from django.contrib.auth import authenticate,login,logout

def home(request):
    uname=""
    if request.method=='POST' and 'submit' in request.POST:
        submit = request.POST['submit']
        if submit=="sign-out":
            logout(request)
    if '_auth_user_id' in request.session:
        uname=sm.UserSocialAuth.objects.get(
            user_id=int(request.session['_auth_user_id'])
        ).user
    return render(request,'home.html',{'uname':uname})
from django.conf import settings
import requests


def homepage(request):
    context = {}

    if request.method == "POST":
        api_address = settings.API_URL
        city = request.POST.get("city", None)

        if city is not None:
            url = api_address + "&q=" + city
            response = requests.get(url).json()
            formatted_data = {
                "city": city,
                "temp": response["main"]["temp"],
            }

            context.update({'response': formatted_data})

        else:
            # render message here
            pass

    return render(request, 'login_api/homepage.html', context)