from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MockTest
from .serializers import MockTestSerializer

class MockTestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        mock_tests = MockTest.objects.all()
        serializer = MockTestSerializer(mock_tests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MockTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MockTestDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MockTest.objects.get(pk=pk)
        except MockTest.DoesNotExist:
            raise None

    def get(self, request, pk, *args, **kwargs):
        mock_test = self.get_object(pk)
        if mock_test:
            serializer = MockTestSerializer(mock_test)
            return Response(serializer.data)
        return Response({'error': 'Mock test not found'}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk, *args, **kwargs):
        mock_test = self.get_object(pk)
        if mock_test:
            serializer = MockTestSerializer(mock_test, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Mock test not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        mock_test = self.get_object(pk)
        if mock_test:
            mock_test.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Mock test not found'}, status=status.HTTP_404_NOT_FOUND)
