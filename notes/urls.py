from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.homeHandler, name='homeHandler'),
    path('login/', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('<subject>/topics/', views.topics, name='topics'),
    path('search/', views.search, name='search'),
    path('<subject>/upload/', views.upload, name='upload'),
    path('<subject>/<chapter>/topics/', views.files, name='files'),
]
