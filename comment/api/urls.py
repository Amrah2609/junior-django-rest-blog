from rest_framework.routers import DefaultRouter
from comment.api.views import CommentViewSet

app_name = 'comment'

router = DefaultRouter()
router.register('', CommentViewSet, basename='comment')

urlpatterns = router.urls
