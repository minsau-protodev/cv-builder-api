from rest_framework import serializers
from .models import Curriculum


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = [
            "uuid",
            "updated_at",
            "name",
            "title",
            "subtitle",
            "description",
        ]
