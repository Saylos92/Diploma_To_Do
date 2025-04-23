from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import TaskViewSet, CategoryViewSet, PriorityViewSet, UsersViewSet

router_v1 = DefaultRouter()
router_v1.register(r'tasks', TaskViewSet, basename='tasks')
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'priority', PriorityViewSet)
router_v1.register(r'users', UsersViewSet, basename='users')

urlpatterns = router_v1.urls

urlpatterns += [
    path('token/', views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

