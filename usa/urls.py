from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from usaapi.views.state import States



router = routers.DefaultRouter(trailing_slash=False)

router.register(r"states", States, "states")

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework"))
] 

