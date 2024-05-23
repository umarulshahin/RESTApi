from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.Serializer):
    
    username =serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    
    def validate(self,data):
        
        if data["username"]:
            if User.objects.filter(username=data["username"]).exists():
                raise serializers.ValidationError("User Alredy exist")
        if data["email"]:
            if User.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("Email alredy exist")
        return data
    
    def create(self,validated_data):
        user=User.objects.create(username=validated_data["username"],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
class LoginSerializer(serializers.Serializer):
     username=serializers.CharField()
     password=serializers.CharField()
         
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']

class PeopleSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_info =serializers.SerializerMethodField()
    class Meta:
        model = People
        fields = '__all__'
        depth = 1  
    def get_team_info(self,obj):
        
        return "Extra serializerFeild"
    
    def validate(self,data):
        spl_char="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        if any(let in spl_char for let in data['name']):
            raise serializers.ValidationError("Name should not have any special charactors")
        if data['age']<18:
            raise serializers.ValidationError("age Should not be less than 18")
        return data