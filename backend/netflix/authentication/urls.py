from django.urls import path
from .views import UserMovieListViewSet, SignupView, LoginView, LogoutView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', ProfileView.as_view(), name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/add_movie/', UserMovieListViewSet.as_view({'post': 'add_movie'}), name='user_add_movie'),
    path('user/remove_movie/', UserMovieListViewSet.as_view({'delete': 'remove_movie'}), name='user_remove_movie'),
    path('user/list_movies/', UserMovieListViewSet.as_view({'get': 'my_movies'}), name='user_list_movies'),
]