from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import PeopleSerializer,RegisterSerializer,LoginSerializer
from .models import People
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegisterApi(APIView):
    
    def post(self,request):
        
        data_=request.data
        serializer=RegisterSerializer(data=data_)
        
        
        if not serializer.is_valid():
            
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'message':"User created"},status=status.HTTP_201_CREATED)
    
class LoginApi(APIView):
    permission_classes=[]
    def post(self,request):
        
        data_=request.data
        serializer = LoginSerializer(data=data_)
        if not serializer.is_valid():
            return Response({"message":serializer.errors},status=status.HTTP_404_NOT_FOUND)
        user=authenticate(username=serializer.data['username'],password=serializer.data["password"])
        print(user)
        if not user:
            return Response({"message":"invalid User Details"},status=status.HTTP_404_NOT_FOUND)
        token,_=Token.objects.get_or_create(user=user)
        return Response({"messages":"Login succesfully",'token':str(token)},status=status.HTTP_201_CREATED)

class peopleAuth(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
  
    def get(self,request):
        
        people_data = People.objects.filter(team__isnull=False)
        serializer = PeopleSerializer(people_data, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        return Response("This is class based postmethod APIView ")
      

  
class ClassPerson(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        
        people_data = People.objects.filter(team__isnull=False)
        serializer = PeopleSerializer(people_data, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        return Response("This is class based postmethod APIView ")
    
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
        people_data = People.objects.filter(team__isnull=False)
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
    
    
class PeopleViewSets(viewsets.ModelViewSet):
    
    serializer_class = PeopleSerializer
    queryset=People.objects.all()
    
    def list(self,request):
        
        search=request.GET.get("search")
        queryset=self.queryset
        
        if search:
            
            queryset=queryset.filter(name__startswith=search)
        serializer = PeopleSerializer(queryset,many=True)
        return Response({'status code':200,'data':serializer.data},status=status.HTTP_204_NO_CONTENT)