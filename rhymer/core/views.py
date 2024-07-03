from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *


class AllWordsAPIView(generics.ListAPIView):
    serializer_class = WordsSerializer

    def get_queryset(self):
        word = self.kwargs.get('word')
        if word and len(word) >= 3:
            end_sequence = word[-3:]
            return AllWords.objects.filter(word__endswith=end_sequence).exclude(word=word)
        elif word and len(word) >= 2:
            end_sequence = word[-2:]
            return AllWords.objects.filter(word__endswith=end_sequence).exclude(word=word)
        return AllWords.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset,
            many=True
        )
        return Response(serializer.data)