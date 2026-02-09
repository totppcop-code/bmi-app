from rest_framework import viewsets
from .models import BMIRecord
from .serializers import BMIRecordSerializer
from django.http import JsonResponse

class BMiRecordViewSet(viewsets.ModelViewSet):
    queryset = BMIRecord.objects.all()
    serializer_class = BMIRecordSerializer

def health(request):
    return JsonResponse({"status":"ok"})
