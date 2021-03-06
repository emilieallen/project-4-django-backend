from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers

from users.models import User
from pictures.serializers import PictureSerializer

class UserProfileSerializer(serializers.ModelSerializer):

    added_picture = PictureSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'added_picture')


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')