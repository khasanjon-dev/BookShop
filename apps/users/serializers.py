from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
        )
