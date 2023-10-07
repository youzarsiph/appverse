""" URLConf for AppVerse.reviews """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.reviews.views import ReviewViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("reviews", ReviewViewSet, "review")


urlpatterns = [
    path("reviews/", include(router.urls)),
]
