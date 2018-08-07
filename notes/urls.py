from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.home_handler, name='home_handler'),
    path('login/', views.login, name='login'),
    path('maps/', views.maps, name='maps'),
    path('<subject>/topics/', views.topics, name='topics'),
    path('search/', views.search, name='search'),
    path('<subject>/upload/', views.upload, name='upload'),
    path('<subject>/<chapter>/topics/', views.files, name='files'),
    path('detail/<filename>/', views.file_detail, name='file_detail'),
    path('download/<filename>/', views.download_file, name='download_file'),
    path('delete/<filename>/', views.delete_file, name='delete_file'),
    path('<subject>/edit/<filename>/', views.edit_file, name='edit_file'),
]
