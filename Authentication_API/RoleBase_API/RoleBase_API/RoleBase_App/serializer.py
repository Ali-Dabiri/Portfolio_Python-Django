from rest_framework import serializers
from django.contrib.auth import get_user_model

UserLogin_Model = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin_Model
        fields = '__all__'

    def create(self, validated_data):
        user = UserLogin_Model.objects.create_user(**validated_data)
        return user
