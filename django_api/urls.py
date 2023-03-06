from django.contrib import admin
from django.urls import path
from test_app.views import Simple


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', Simple.as_view())
]
