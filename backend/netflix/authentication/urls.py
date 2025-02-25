from django.urls import path
from .views import UserMovieListViewSet, CustomTokenObtainPairView, \
    CustomRefreshTokenView, logout, register

urlpatterns = [
    path('signup/', register, name='signup'),
    path('logout/', logout, name='logout'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('user/add_movie/', UserMovieListViewSet.as_view({'post': 'add_movie'}), name='user_add_movie'),
    path('user/remove_movie/', UserMovieListViewSet.as_view({'delete': 'remove_movie'}), name='user_remove_movie'),
    path('user/list_movies/', UserMovieListViewSet.as_view({'get': 'my_movies'}), name='user_list_movies'),
]