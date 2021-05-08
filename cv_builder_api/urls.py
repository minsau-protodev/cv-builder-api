from django.contrib import admin
from django.urls import path, include
from users.views import UserAPIView, RegisterView
from structure.views import CurriculumViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"api/cv", CurriculumViewSet, basename="cv")
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/user", UserAPIView.as_view(), name="user"),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
