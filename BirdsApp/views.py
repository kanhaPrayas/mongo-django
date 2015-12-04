from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import Connection
from models import Birds
from serializers import BirdsSerializer
from rest_framework import status
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import BusinessCardInfo
from .serializers import BusinessCardInfoSerializer
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bson import json_util, ObjectId
import json
from mongoengine import *
'''



@csrf_exempt
@api_view(['GET','POST','DELETE'])
def birds(request):
    #connect to our local mongodb
    db = Connection('localhost',27017)
    #get a connection to our database
    dbconn = db.birds
    birdCollection = dbconn['Birds']

    if request.method == 'GET':
        birds = []
        for b in birdCollection.find():
            bird = Birds(b["_id"],b["name"],b["family"],b["continents"])
            birds.append(bird)
        serializedList = BirdsSerializer(birds, many=True)
        return Response(serializedList.data)
    elif request.method == 'POST':
        #get data from the request and insert the record
        name = request.POST["name"]
        family = request.POST["family"]
        continents = request.POST["continents"]
        try:
            birdCollection.insert({"name" : name, "family": family, "continents":continents})
        except:
            return Response({ "ok": "false" })
        return Response({ "ok": "true" }, status=status.HTTP_201_CREATED)





@csrf_exempt
@api_view(['GET','DELETE'])
def bird(request):
    #connect to our local mongodb
    db = Connection('localhost',27017)
    #get a connection to our database
    dbconn = db.birds
    birdCollection = dbconn['Birds']
    if request.method == 'GET':
        try:
            id = request.GET["id"]
            for b in birdCollection.find():
                if b["_id"].get('id') == id:
                    bird = Birds(b["id"],b["name"],b["family"],b["continents"])
                    serializedList = BirdsSerializer(bird)
                    return Response(serializedList.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception,e:
            return Response({ "ok": "false" })
    elif request.method == 'DELETE':
        #get data from the request and insert the record
        id = request.POST["id"]
        try:
            birdCollection.remove({"id" : id})
        except Exception,e:
            return Response({ "ok": "false" })
        return Response(status=status.HTTP_204_NO_CONTENT)










