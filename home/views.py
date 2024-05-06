from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is home page")

def yo(request):
    return HttpResponse("yo")

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def contact(request):
    contact_text = "This is the contact page."
    return Response({"message": contact_text})
@api_view()
def about(request):
    about_text = "This is the about page."
    return Response({"message": about_text})
