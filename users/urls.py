from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
]
