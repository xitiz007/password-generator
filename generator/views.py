from django.shortcuts import render
from django.http import HttpResponse
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 0))
    _length = length
    if length < 6:
        pass
    generated_password = ""
    letters = ascii_lowercase

    if request.GET.get('uppercase'):
        letters += ascii_uppercase
        generated_password += random.choice(ascii_uppercase)
        length -= 1
    if request.GET.get('digits'):
        letters += digits
        generated_password += random.choice(digits)
        length -= 1
    if request.GET.get('specialcharacters'):
        letters += punctuation
        generated_password += random.choice(punctuation)
        length -= 1

    for _ in range(length):
        generated_password += random.choice(letters)
    
    return render(request, 'generator/password.html', {'generated_password': generated_password, 'length' : _length})