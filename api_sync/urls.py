from django.urls import path

from . import views

app_name = 'api_sync'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/post/', views.PostView.as_view(), name="post")
]
