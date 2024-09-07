from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_phone(self, value):
        if Student.objects.filter(phone=value).exists():
            raise serializers.ValidationError('Phone number already exists')
        return value
