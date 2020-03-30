from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PropietarioSerializer, InquilinoSerializer
from .models import Propietario, Inquilino
# Create your views here.


class PropietarioView(generics.ListAPIView):
    serializer_class = PropietarioSerializer
    queryset = Propietario.objects.all()


class PropietarioRUD(APIView):
    serializer_class = PropietarioSerializer
    queryset = Propietario.objects.all()

    def get(self, request, pk=None):
        queryset = self.queryset
        user = get_object_or_404(queryset, user__pk=pk)
        serializer = PropietarioSerializer(user, many=False)
        return Response(serializer.data)

    def post(self, request, pk=None):
        print(pk, request.user, request.data)
        serializer_context = {
            'user': request.user,
            'request': request
        }
        serializer_data = request.data.get('propietario', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InquilinoView(generics.ListAPIView):
    serializer_class = InquilinoSerializer
    queryset = Inquilino.objects.all()


class InquilinoRUD(APIView):
    serializer_class = InquilinoSerializer
    queryset = Inquilino.objects.all()

    def get(self, request, pk=None):
        queryset = self.queryset
        user = get_object_or_404(queryset, user__pk=pk)
        serializer = InquilinoSerializer(user, many=False)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer_context = {
            'user': request.user,
            'request': request
        }
        serializer_data = request.data.get('inquilino', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)







