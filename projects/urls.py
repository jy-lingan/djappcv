from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.projects, name='projects'),
    path('product/<str:pk>', views.project, name='project'),
]
