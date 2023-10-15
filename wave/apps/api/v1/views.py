from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def index(request):
    return Response({'success': True}, status=status.HTTP_200_OK)