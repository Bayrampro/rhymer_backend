from rest_framework import serializers

from .models import AllWords


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllWords
        fields = ('word',)
