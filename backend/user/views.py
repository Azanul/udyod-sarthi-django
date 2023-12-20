from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EndUser
from .serializers import EndUserSerializer

class EndUserListCreateView(APIView):
    def get(self, request, format=None):
        endusers = EndUser.objects.all()
        serializer = EndUserSerializer(endusers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EndUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EndUserRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return EndUser.objects.get(pk=pk)
        except EndUser.DoesNotExist:
            raise None

    def get(self, request, pk, format=None):
        enduser = self.get_object(pk)
        serializer = EndUserSerializer(enduser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        enduser = self.get_object(pk)
        serializer = EndUserSerializer(enduser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        enduser = self.get_object(pk)
        enduser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
