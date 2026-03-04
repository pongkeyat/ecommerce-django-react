from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializers):
    user = serializers.SerializerMethodField()

    class Meta:
        model: User
        fields = [
            "id", "username", "email", "role", "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_field = ["id"]

    def create(self,validate_data):
        user = User(
            username = validate_data["username"],
            email = validate_data["email"],
            role = validate_data["role"]
        )
        user.set_password(validate_data["password"])
        user.save()
        return user

