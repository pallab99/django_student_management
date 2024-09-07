from django.db.models import Q


def generate_filter(request):
    search_query = request.query_params.get('search', None)
    age_query = request.query_params.get('age', None)

    filters = Q()
    if search_query:
        filters &= Q(name__icontains=search_query)
    if age_query:
        age_query = int(age_query)
        filters &= Q(age__gte=age_query)
    return filters
