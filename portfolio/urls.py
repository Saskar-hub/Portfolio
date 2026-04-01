from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from . import views

router = DefaultRouter()
router.register(r'settings', views.SiteSettingsViewSet)
router.register(r'hero', views.HeroSectionViewSet)
router.register(r'about', views.AboutViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'contact', views.ContactMessageViewSet)
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'experience', views.ExperienceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    
    # Custom Admin (Django Templates)
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/hero/', views.admin_hero, name='admin_hero'),
    path('dashboard/about/', views.admin_about, name='admin_about'),
    path('dashboard/settings/', views.admin_settings, name='admin_settings'),
    path('dashboard/list/<str:model_name>/', views.admin_list, name='admin_list'),
    path('dashboard/add/<str:model_name>/', views.admin_add_item, name='admin_add_item'),
    path('dashboard/edit/<str:model_name>/<int:pk>/', views.admin_edit_item, name='admin_edit_item'),
    path('dashboard/delete/<str:model_name>/<int:pk>/', views.admin_delete_item, name='admin_delete_item'),
    
    # Auth for Custom Admin
    path('dashboard/login/', auth_views.LoginView.as_view(template_name='portfolio/admin/login.html'), name='login'),
    path('dashboard/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
