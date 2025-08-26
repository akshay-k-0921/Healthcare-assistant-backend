from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('chatbot.urls')),
    path('api/users/', include('users.urls')),

]
