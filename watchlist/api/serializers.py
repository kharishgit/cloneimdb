from multiprocessing.sharedctypes import Value
from rest_framework import serializers

from watchlist.models import movie

class movieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return movie.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    def validate_name(self, attrs):
        if len(attrs) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long")
        else:
            return attrs
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Both name and description must not be the same")
        else:
            return data
                   
    