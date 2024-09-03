from rest_framework.pagination import PageNumberPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    max_page_size = 10


