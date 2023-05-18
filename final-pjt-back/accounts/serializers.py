from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = UserSerializer(many=False, read_only=True)  # this is add by myself.
    class Meta:
        model = Token
        fields = ('key', 'user')   # there I add the `user` field ( this is my need data ).
