from django.contrib import admin
from django.urls import include, path
from postings.views import PostingViewSet
from rest_framework.routers import DefaultRouter

from .views import home  # <--- import from views.py

router = DefaultRouter()
router.register("postings", PostingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", home),  # homepage
]
