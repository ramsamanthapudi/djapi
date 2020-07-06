from rest_framework import pagination

class QuotePagination(pagination.PageNumberPagination):
    page_size = 2
