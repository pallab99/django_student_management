from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, UserProfile
from .serializer import UserSerializer, UserProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.


class UserView(viewsets.ViewSet):
    def list(self, request):
        user_list = User.objects.all()
        serializer = UserSerializer(user_list, many=True)
        return Response({"isSuccess": True, "message": "Successfully retrieved user list", "data": serializer.data})

    def retrieve(self, _, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response({"isSuccess": True, "message": "Successfully retrieved user", "data": serializer.data})

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Save the user
            user = serializer.save()

        # Create the associated UserProfile
            profile_data = {
                'user': user.id,
                'phone_number': request.data.get('phone', ''),
                'address': request.data.get('address', '')
            }
            profile_serializer = UserProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
            else:
                return Response({
                    "isSuccess": False,
                    "message": "Failed to create user profile",
                    "errors": profile_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "isSuccess": True,
                "message": "Successfully created user and profile",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "isSuccess": False,
            "message": "Failed to create user",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = get_object_or_404(
            User, pk=pk)
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"isSuccess": True, "message": "Successfully updated user", "data": serializer.data})
        return Response({"isSuccess": False, "message": "Failed to update user", "errors": serializer.errors})


class UserProfileView(viewsets.ViewSet):
    def list(self, request):
        user_profile_list = UserProfile.objects.select_related('user').all()
        serializer = UserProfileSerializer(user_profile_list, many=True)
        return Response({"isSuccess": True, "message": "Successfully retrieved user profile list", "data": serializer.data})

    def retrieve(self, _, pk=None):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user_profile)
        return Response({"isSuccess": True, "message": "Successfully retrieved user profile", "data": serializer.data})
