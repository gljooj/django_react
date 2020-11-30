from leads.models import Lead, ClassName, Students
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, ClassNameSerializer, StudentsSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadSerializer

class ClassNameViewSet(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClassNameSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentsSerializer