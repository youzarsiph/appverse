""" URLConf for appverse.orders """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.orders.views import UserOrdersViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("orders", UserOrdersViewSet, "preorder")


urlpatterns = [
    path("", include(router.urls)),
]
