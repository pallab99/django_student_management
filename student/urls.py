from .views import StudentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentView, basename='student')
urlpatterns = router.urls
