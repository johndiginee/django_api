from django.contrib import admin
from django.urls import path, include
from test_app.views import SimpleViewset

from rest_framework.routers import DefaultRouter

# Initializing DefaultRouter
router = DefaultRouter()
router.register("simple-viewset", SimpleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
