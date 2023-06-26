from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Author, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = Author
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'dob', 'mobile')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'