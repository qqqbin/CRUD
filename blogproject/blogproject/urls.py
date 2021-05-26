from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.main, name='main'),
    path('detail/<str:id>/', blogapp.views.detail, name='detail'),
    path('read/', blogapp.views.read, name='read'),
    path('write/create/', blogapp.views.create, name='create'),
    path('edit/<str:id>/', blogapp.views.edit, name='edit'),
    path('delete/<str:id>/', blogapp.views.delete, name='delete'),
]
