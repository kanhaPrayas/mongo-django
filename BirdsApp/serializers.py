from rest_framework import serializers
from models import Birds

class BirdsSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=50)
    name = serializers.CharField(required=True, max_length=100)
    family = serializers.CharField(required=False, max_length=200)
    continents = serializers.CharField(required=False, max_length=200)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.id = attrs.get('id', instance.id)
            instance.name = attrs.get('name', instance.name)
            instance.family = attrs.get('address', instance.family)
            instance.continents = attrs.get('address', instance.continents)
            return instance
        return Birds(attrs.get('id'),attrs.get('name'),attrs.get('family'))