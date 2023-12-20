from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import BasePermission
from django.db.models import Q

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.created_by == request.user
    
class JobList(APIView):
    def get(self, request):
        jobs = Job.objects.reverse()
        search_term = request.query_params.get('search', '')
        jobs = Job.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(location__icontains=search_term) |
            Q(company__icontains=search_term) |
            Q(salary_min__icontains=search_term) |
            Q(salary_max__icontains=search_term) |
            Q(posted_at__icontains=search_term) |
            Q(application_deadline__icontains=search_term)
        )
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetail(APIView):
    def get_object(self, job_id):
        try:
            return Job.objects.get(pk=job_id)
        except Job.DoesNotExist:
            return None

    def get(self, request, job_id):
        job = self.get_object(job_id)
        if job:
            serializer = JobSerializer(job)
            return Response(serializer.data)
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, job_id):
        job = self.get_object(job_id)
        if job:
            serializer = JobSerializer(job, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, job_id):
        job = self.get_object(job_id)
        if job:
            job.delete()
            return Response({'message': 'Job deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
