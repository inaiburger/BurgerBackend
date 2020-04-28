from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from people.models import UserInfo
from people.serializers import UserInfoSerializer
from people.permissions import IsOwnerProfileOrReadOnly


class UserInfoListCreateView(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

