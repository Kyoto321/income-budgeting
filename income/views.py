from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from .models import Income
from rest_framework import permissions
from .permissions import IsOwner


# Create your views here.
class IncomeList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



class IncomeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    
    lookup_field = "id"

    """
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    """
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)






