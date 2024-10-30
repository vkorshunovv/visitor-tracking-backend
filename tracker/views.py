from django.shortcuts import render
from rest_framework import viewsets
from .models import Visitor
from .serializers import VisitorSerializer

class VisitorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Visitor.objects.all().order_by('-timestamp')
    serializer_class = VisitorSerializer
