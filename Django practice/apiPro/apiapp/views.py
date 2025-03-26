from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def getAll(request):
    infoData=info.objects.all()
    dt=inf(infoData,many=True)
    return Response(data=dt.data)

@api_view(['GET'])
def getId(request,id):
    try:
        stid=info.objects.get(id=id)
    except info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    sr=inf(stid)
    return Response(data=sr.data)

@api_view(["GET", "DELETE"])
def deleteId(request,id):
    try:
        stid=info.objects.get(id=id)
    except info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        sr=inf(stid)
        return Response(data=sr.data)
    if request.method =='DELETE':
        info.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def inData(request):
   if request.method == 'POST':
       sr=inf(data=request.data)
       if sr.is_valid():
           sr.save()
           return Response(status=status.HTTP_201_CREATED)
       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['GET','PUT'])
def updata(request,id):
    try:
        stid=info.objects.get(id=id)
    except info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        sr = inf(stid)
        return Response(data=sr.data)
    if request.method == 'PUT':
        sr=inf(data=request.data,instance=stid)
        if sr.is_valid():
            sr.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

