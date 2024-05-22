from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import PeopleSerializer
from .models import People

@api_view(['GET','POST','PUT','DELETE'])
def index(request):
    
    if request.method == "GET":
        userData={
            "name":"Shahin",
            "age":24,
            "Job":"IT Profession" 
        }
        
        return Response(userData)
    elif request.method == "POST":
        return Response("This is a POST method")
    elif request.method == "PUT":
        return Response("This is a PUT method")
    
@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def PersonData(request):
    if request.method == "GET":
        people_data = People.objects.all()
        serializer = PeopleSerializer(people_data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        
        data=request.data
        print(data)
        obj =People.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        
        data=request.data
        obj =People.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data=request.data
        obj=People.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"Person deleted"})