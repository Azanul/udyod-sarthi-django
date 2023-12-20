# serializers.py

from rest_framework import serializers
from .models import Course, Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    skills_taught = SkillSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'skills_taught']
