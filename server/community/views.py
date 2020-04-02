from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated

from .serializers import CommunitySerializer
from .models import Community
# Create your views here.


class CommunityView(generics.ListAPIView):
    serializer_class = CommunitySerializer
    queryset = Community.objects.all()
    permission_classes = [IsAuthenticated]