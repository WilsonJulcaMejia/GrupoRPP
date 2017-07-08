from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import New
from .paginations import StandardResultsSetPagination
from .serializers import ListNewSerializer


class ListNewsAPI(ListAPIView):
    serializer_class = ListNewSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return New.objects.filter(is_enabled=True).order_by('-created_at')
