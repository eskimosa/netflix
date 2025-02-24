from django.urls import path
from .views import SignupView, LoginView, LogoutView, UserMovieListViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/add_movie/', UserMovieListViewSet.as_view({'post': 'add_movie'}), name='user_add_movie'),
    path('api/user/remove_movie/', UserMovieListViewSet.as_view({'delete': 'remove_movie'}), name='user_remove_movie'),
    path('api/user/list_movies/', UserMovieListViewSet.as_view({'get': 'my_movies'}), name='user_list_movies'),
]