from rest_framework import viewsets
from rest_framework.response import Response
from .serialiazer import StudentSerializer
from .models import Student
from django.shortcuts import get_object_or_404
from .list_filter import generate_filter


class StudentView(viewsets.ViewSet):
    def list(self, request):
        filters = generate_filter(request)
        print(filters)
        if filters:
            student_list = Student.objects.filter(filters)
            serializer = StudentSerializer(student_list, many=True)
        else:
            student_list = Student.objects.all()
            serializer = StudentSerializer(student_list, many=True)
        return Response({"isSuccess": True, "message": "Successfully retrieved student list", "data": serializer.data})

    def retrieve(self, _, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response({"isSuccess": True, "message": "Successfully retrieved student", "data": serializer.data})

    def create(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"isSuccess": True, "message": "Successfully created student", "data": serializer.data})
        return Response({"isSuccess": False, "message": "Failed to create student", "errors": serializer.errors}, status=400)

    def update(self, request, pk=None):
        student = get_object_or_404(
            Student, pk=pk)
        data = request.data
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"isSuccess": True, "message": "Successfully updated student", "data": serializer.data})
        return Response({"isSuccess": False, "message": "Failed to update student", "errors": serializer.errors})

    def destroy(self, _, pk=None):
        student = get_object_or_404(
            Student, pk=pk)
        student.delete()
        return Response({"isSuccess": True, "message": "Successfully deleted student", "data": None})
