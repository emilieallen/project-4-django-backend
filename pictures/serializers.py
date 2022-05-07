from rest_framework import serializers

from .models import Picture

class PictureSerializer(serializers.ModelSerializer):
    """ Serializer of a picture """

    class Meta:
        model = Picture
        fields = '__all__'
