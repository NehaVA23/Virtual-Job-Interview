# api/serializers.py

from rest_framework import serializers
from .models import InterviewPreference, Question

class InterviewPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewPreference
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
