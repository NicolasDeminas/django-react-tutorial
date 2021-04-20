from django.urls import path
from .views import RoomViews, CreateRoomView, GetRoom

urlpatterns = [
    path('room', RoomViews.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view())
]
