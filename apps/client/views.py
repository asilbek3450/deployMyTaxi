import imp

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


# GET, POST
class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# GET_ID, PUT
class RetrieveClientAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


def LoginPage(request):
    return render(request, 'login.html')


def HomePage(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def News(request):
    return render(request, 'news.html')


def ContactUs(request):
    return render(request, 'contact.html')
