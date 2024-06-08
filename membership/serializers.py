from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','username', 'age', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        member = Member.objects.create_user(**validated_data)
        return member