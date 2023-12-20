from rest_framework import serializers
from .models import EndUser

class EndUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        fields = ['id', 'username', 'password', 'email', 'saved_query']
