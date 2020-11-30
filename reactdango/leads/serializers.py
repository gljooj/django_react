from rest_framework import serializers
from leads.models import Lead, ClassName, Students

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields='__all__'

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields='__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields='__all__'