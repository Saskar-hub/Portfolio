from django.urls import path
from . import views

urlpatterns = [
    # Public Website
    path('', views.home, name='home'),
    path('contact/', views.contact_form, name='contact_form'),
    
    # Custom Admin Dashboard
    path('admin-dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/logout/', views.admin_logout, name='admin_logout'),
    
    # CRUD for Projects
    path('admin-dashboard/projects/', views.project_list, name='project_list'),
    path('admin-dashboard/projects/add/', views.project_add, name='project_add'),
    path('admin-dashboard/projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('admin-dashboard/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # CRUD for Skills
    path('admin-dashboard/skills/', views.skill_list, name='skill_list'),
    path('admin-dashboard/skills/add/', views.skill_add, name='skill_add'),
    path('admin-dashboard/skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('admin-dashboard/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Experience & Education
    path('admin-dashboard/experience/', views.experience_list, name='experience_list'),
    path('admin-dashboard/experience/add/', views.experience_add, name='experience_add'),
    path('admin-dashboard/experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    
    # Messages
    path('admin-dashboard/messages/', views.message_list, name='message_list'),
    path('admin-dashboard/messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    
    # About section dynamic editing
    path('admin-dashboard/about/', views.about_edit, name='about_edit'),
]
