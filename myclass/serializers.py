from rest_framework import serializers
from .models import studentData


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentData
        fields = ['id','name','grade','rollno','age','fathersname']