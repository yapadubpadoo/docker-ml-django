from rest_framework import viewsets

from django.utils.encoding import force_text
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from .models import MoviesSuggester

class Hello(APIView):
    def get(self, request):
        return Response({"hello": "world"})
    

# your ml class here
class MoviesSuggestionView(APIView):
    def get(self, request):
        from_name = request.GET.get('from', 'Star Wars (1977)')
        movies_list = MoviesSuggester().suggest(from_name)
        return Response({
            "suggested_movies":movies_list
            })
    