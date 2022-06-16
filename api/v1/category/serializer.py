from rest_framework import serializers
from blog.models import Category


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
