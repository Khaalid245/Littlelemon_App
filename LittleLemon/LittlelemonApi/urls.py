from django.urls import path
from .  import views

urlpatterns=[
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view())
]