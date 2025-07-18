from django.urls import path
# users/urls.py
from .views import register_user, CustomLoginView, LogoutView, list_users
from rest_framework_simplejwt.views import TokenObtainPairView

# ⛔ remove LogoutView if it's not defined

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', CustomLoginView.as_view(), name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', list_users, name='list_users'),  # <-- This is for /api/users/



]
