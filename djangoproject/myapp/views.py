from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('<h2> welcome to django </h2>')

def aboutpageview(request):
    return HttpResponse('<h2> about us </h2>')

def contactpageview(request):
    return HttpResponse('<h2> contact us </h2>')

