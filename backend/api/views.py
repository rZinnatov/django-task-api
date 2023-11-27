from django_filters import FilterSet, DateFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)

from .models import Task
from .serializers import TaskSerializer


class TaskFilter(FilterSet):
    """
    Provides the filtering functionality for Task model
    """

    created_at_from = DateFilter(field_name='created_at', lookup_expr='date__gte')
    created_at_to = DateFilter(field_name="created_at", lookup_expr='date__lte')

    class Meta:
        model = Task
        fields = [
            'status',
            'created_at_from',
            'created_at_to',
        ]

class TaskViewSet(ModelViewSet,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  ListModelMixin):
    """
    API for Task model. Provides full CRUD functinality.
    """

    filterset_class = TaskFilter
    serializer_class = TaskSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.select_related("user").filter(user=self.request.user).order_by('created_at')
