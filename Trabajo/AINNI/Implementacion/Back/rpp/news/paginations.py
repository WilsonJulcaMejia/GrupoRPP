from rest_framework.pagination import PageNumberPagination

__author__ = 'lucaru9'


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
