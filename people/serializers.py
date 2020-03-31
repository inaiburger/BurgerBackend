from rest_framework import serializers
from people.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'

