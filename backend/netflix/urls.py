from django.urls import path
from .views import MovieViewSet

urlpatterns = [
    path('movies/', MovieViewSet.as_view({'get': 'list'}), name='movies'),
    # path('get_movies/', MovieApiFetchViewSet.as_view({'get': 'list'}), name='get_movies'),
]