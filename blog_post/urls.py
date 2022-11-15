from django.urls import path
from blog_post.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns = router.urls