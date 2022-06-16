from rest_framework import serializers
from blog.models import Project


class ProjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
