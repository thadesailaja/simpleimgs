from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def mrggreet(rquest):
    return HttpResponse('''
    <h2><i>Good morning to all</i></h2>
    ''')