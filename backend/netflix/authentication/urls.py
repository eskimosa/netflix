from django.urls import path
from .views import UserMovieListViewSet, CustomTokenObtainPairView, \
    CustomRefreshTokenView, logout, register

urlpatterns = [
    path('signup/', register, name='signup'),
    path('logout/', logout, name='logout'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('api/user/add_movie/', UserMovieListViewSet.as_view({'post': 'add_movie'}), name='user_add_movie'),
    path('api/user/remove_movie/', UserMovieListViewSet.as_view({'delete': 'remove_movie'}), name='user_remove_movie'),
    path('api/user/list_movies/', UserMovieListViewSet.as_view({'get': 'my_movies'}), name='user_list_movies'),
]