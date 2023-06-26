from django.urls import path, include
from rest_framework import routers
from app import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.SimpleRouter()
router.register(r'users', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [    path('auth/', obtain_auth_token),]
urlpatterns += router.urls