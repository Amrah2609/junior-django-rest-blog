from rest_framework.routers import DefaultRouter
from post.api.views import PostViewSet

app_name = 'post'

router = DefaultRouter()
router.register('', PostViewSet, basename='post')

urlpatterns = router.urls
