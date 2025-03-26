from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ml_model import predict_solution

@api_view(['POST'])
def classify_query(request):
    user_query = request.data.get('query', '')

    if not user_query:
        return Response({"error": "Query cannot be empty"}, status=400)

    result = predict_solution(user_query)
    return Response(result)


