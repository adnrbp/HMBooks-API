"""Health Checks View """

# Django Rest
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(request):
    data = {"api": "OK"}
    return Response(data)