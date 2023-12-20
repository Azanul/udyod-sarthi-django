from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from django.db.models import Q

class CourseList(APIView):
    def get(self, request):
        search_term = request.query_params.get('search', '')
        courses = Course.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(skills_taught__name__icontains=search_term)
        )
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    def get_object(self, course_id):
        try:
            return Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return None

    def get(self, request, course_id):
        course = self.get_object(course_id)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, course_id):
        course = self.get_object(course_id)
        if course:
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, course_id):
        course = self.get_object(course_id)
        if course:
            course.delete()
            return Response({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)