from django.urls import path, include
from rest_framework import routers
from colegioAPI import views


router = routers.DefaultRouter()
router.register(r'grados',views.GradoViewSet)
router.register(r'persona',views.PersonaviewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('login/', views.login.as_view(), name='login'),
]