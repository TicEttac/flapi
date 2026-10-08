from rest_framework import serializers
from base.models import Score

class scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score', 'pseudo']
