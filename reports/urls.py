""" URLConf for AppVerse.reports """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from appverse.reports.views import ReportViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("reports/", include(router.urls)),
]
