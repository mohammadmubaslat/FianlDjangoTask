from django.contrib.auth import get_user_model
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from app.permissions import IsCreationOrIsAuthenticated
from .serializers import AuthorSerializer, BookSerializer
from .models import  Books



class AuthorViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)



class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer