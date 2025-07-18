from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import CustomTokenView  # Your custom JWT view (if any)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # User-related APIs (e.g., register, login)
    path('api/users/', include('users.urls')),

    # Article/content-related APIs
    path('api/', include('cmsapi.urls')),

    # JWT Authentication
    path('api/token/', CustomTokenView.as_view(), name='token_obtain_pair'),  # ✅ Use only ONE
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
