from django.urls import path

from . import views

app_name = "appxd"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.ImageView.as_view(), name="image"),
    path('<int:image_id>/delete_rectangle/<int:rectangle_id>/', views.delete_rectangle, name='delete_rectangle'),
    path('<int:image_id>/add_rectangle/', views.add_rectangle, name='add_rectangle'),
]