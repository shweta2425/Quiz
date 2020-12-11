from rest_framework import serializers
from .models import ShortExam


# serializer class for notes
class ShortExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortExam
        fields = '__all__'