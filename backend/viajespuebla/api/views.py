from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Viaje, Profile
from api.serializers import ViajeSerializer, UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def viaje_list(request, format=None):
    """
    List all code serie, or create a new serie.
    """
    print (request)
    if request.method == 'GET':
        viajes = Viaje.objects.all()
        serializer = ViajeSerializer(viajes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
<<<<<<< HEAD

        print(request.data)
        #data = JSONParser().parse(request.data)

        serializer = ViajeSerializer(data=request.data)
=======
        #data = JSONParser().parse(request)
        serializer = ViajeSerializer(data=request)
>>>>>>> 3c7b126eb925f87c11ca1835d392c111461436c5
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def viaje_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        viaje = Viaje.objects.get(pk=pk)
    except Viaje.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ViajeSerializer(viaje)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ViajeSerializer(viaje, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        viaje.delete()
        return HttpResponse(status=204)


@csrf_exempt
@api_view(['GET', 'POST'])

def profile_list(request, format=None):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many = True)
        return JSONResponse(serializer.data, status = 200)

    elif request.method == 'POST':



        #data = JSONParser().parse(json_data)
        #Display parameters
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def profile_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(viaje, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profile.delete()
        return HttpResponse(status=204)


@csrf_exempt
def suscribe_to_trip(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        user = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        user.trips.add(request.GET.get('trip_id'))
        user.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

@csrf_exempt
def user_trips(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        user = Profile.objects.get(pk=pk)
        mytrips = user.trips.all()
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ViajeSerializer(mytrips, many=True)
        return JSONResponse(serializer.data)
    return HttpResponse(status=400)
