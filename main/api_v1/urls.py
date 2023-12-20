from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    CommentViewSet,
    ExpertViewSet,
    LatestPostViewSet,
    TestimonialViewSet,
    ClientViewSet,
    FreeConsultationViewSet,
    MessageViewSet,
)

router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet)
router.register(r"experts", ExpertViewSet),
router.register(r"latest_posts", LatestPostViewSet),
router.register(r"testimonials", TestimonialViewSet),
router.register(r"clients", ClientViewSet)
router.register(r"free_consultations", FreeConsultationViewSet)
router.register(r"messages", MessageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]
