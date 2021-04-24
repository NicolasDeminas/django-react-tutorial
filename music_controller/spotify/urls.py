from django.urls import path
from .views import AuthURL, spotify_callback, is_authenticated

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', is_authenticated.as_view())
]
