from rest_framework import serializers
from blog.models import Person


class PersonSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'