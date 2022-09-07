from django.urls import path
from meetings import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.all_rooms, name="all_rooms"),
	path('new', views.new, name="new")
]
