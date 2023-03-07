from django.contrib import admin
from django.urls import path, include
from test_app.views import SimpleViewset
from django.conf import settings

from rest_framework.routers import DefaultRouter

# Initializing DefaultRouter
router = DefaultRouter()
router.register("simple-viewset", SimpleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns