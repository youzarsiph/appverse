""" URLConf for appverse.reviews """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.reviews.views import UserReviewsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("reviews", UserReviewsViewSet, "review")


urlpatterns = [
    path("", include(router.urls)),
]
