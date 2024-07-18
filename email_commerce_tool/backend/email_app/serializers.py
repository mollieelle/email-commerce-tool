from rest_framework import serializers
from .models import EmailDraft

class EmailDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDraft
        fields = '__all__'
