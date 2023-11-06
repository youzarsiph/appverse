""" URLConf for AppVerse.preorders """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.preorders.views import UserPreOrdersViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("preorders", UserPreOrdersViewSet, "preorder")


urlpatterns = [
    path("", include(router.urls)),
]
