from django.shortcuts import render


def UsersDef(request):
    return render(request, 'account/user_profile.html')
