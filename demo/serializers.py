from rest_framework import serializers
from .models import Course, Note

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','className', 'professor', 'section']
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'date', 'course', 'content']