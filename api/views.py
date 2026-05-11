from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status as drf_status
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-creada_en')
    serializer_class = TareaSerializer


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'ok'}, status=drf_status.HTTP_200_OK)
