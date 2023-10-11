# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
#
# class StudentApiView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get_by_id(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentApiView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

