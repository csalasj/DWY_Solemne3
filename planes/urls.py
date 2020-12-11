from django.urls import path, include
from rest_framework import routers, serializers, viewsets, filters
from .models import Plan
from django_filters.rest_framework import DjangoFilterBackend

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['titulo', 'velocidad', 'minutos', 'canales', 'valor']

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'titulo',]
    search_fields = ['id', 'titulo',]

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]