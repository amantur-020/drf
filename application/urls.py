from rest_framework import routers
from . import views
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)



urlpatterns = [

    path('api/', include(router.urls)),
    path('api/drf/', include('rest_framework.urls')),
    path('api/postlist/', views.PostListAPIView.as_view(), name='postlist'),
    path('api/postapi/', views.PostAPIView.as_view(), name='postapi'),
    path('api/postapi/<int:pk>/', views.PostAPIView.as_view(), name='postapi'),
    path('api/postlistcreate/', views.PostListCreateAPIView.as_view(), name='postlistcreate'),
    path('api/postupdate/<int:pk>/', views.PostUpdateAPIView.as_view(), name='postupdate'),
    path('api/postcrud/<int:pk>/', views.PostCRUD.as_view(), name='postcrud'),
]
