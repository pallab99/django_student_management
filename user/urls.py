from .views import UserView, UserProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView, basename='user')
router.register(r'user-profiles', UserProfileView, basename='user-profile')
urlpatterns = router.urls
