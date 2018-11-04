from django.urls import path
from advert import views


urlpatterns = [
    path('create/', views.AdvertCreate.as_view()),
    path('update/<int:pk>/', views.AdvertUpdate.as_view()),
    path('delete/<int:pk>/', views.AdvertDelete.as_view()),
    path('view/', views.Advertlist.as_view()),
    path('', views.index, name = 'index'),
]
