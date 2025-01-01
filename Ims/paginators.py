from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Кол-во элементов на странице
    page_size_query_param = (
        "page_size"  # Параметр запроса для указания количества элементов на странице
    )
    max_page_size = 10  # Максимальное кол-во элементов на странице