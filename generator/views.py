from django.shortcuts import render
import random
#from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password=''

    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('_!@#$%&()*+^'))

    for char in range(length):
        generated_password += random.choice(characters)
    print(generated_password)
    return render(request, 'password.html', {'password': generated_password})