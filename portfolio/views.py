from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
# views.py
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import (
    Project, Skill, Experience, Education, Testimonial, 
    BlogPost, ContactMessage, About, Category, SkillCategory
)
from .forms import ContactForm, ProjectForm, SkillForm, ExperienceForm, AboutForm
from django.contrib.auth.forms import AuthenticationForm

# --- Public Views ---

def home(request):
    about = About.objects.first()
    categories = Category.objects.all()
    projects = Project.objects.all().order_by('-created_at')
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all().order_by('-order', '-id')
    educations = Education.objects.all().order_by('-order', '-id')
    testimonials = Testimonial.objects.all()
    blogs = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    
    contact_form = ContactForm()
    
    context = {
        'about': about,
        'categories': categories,
        'projects': projects,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'educations': educations,
        'testimonials': testimonials,
        'blogs': blogs,
        'contact_form': contact_form,
    }
    return render(request, 'portfolio/index.html', context)

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your form. Please check again.')
    return redirect('home')

# --- Admin Dashboard Views ---

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_dashboard/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def dashboard(request):
    project_count = Project.objects.count()
    skill_count = Skill.objects.count()
    message_count = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    
    context = {
        'project_count': project_count,
        'skill_count': skill_count,
        'message_count': message_count,
        'unread_messages': unread_messages,
        'recent_messages': recent_messages,
    }
    return render(request, 'admin_dashboard/dashboard.html', context)

# CRUD for Projects
@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard/projects.html', {'projects': projects})

@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'admin_dashboard/project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'admin_dashboard/project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect('project_list')

# CRUD for Skills
@login_required
def skill_list(request):
    skills = Skill.objects.all().order_by('category', 'name')
    return render(request, 'admin_dashboard/skills.html', {'skills': skills})

@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'admin_dashboard/skill_form.html', {'form': form, 'title': 'Add Skill'})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'admin_dashboard/skill_form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('skill_list')

# Experience
@login_required
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'admin_dashboard/experience.html', {'experiences': experiences})

@login_required
def experience_add(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'admin_dashboard/experience_form.html', {'form': form, 'title': 'Add Experience'})

@login_required
def experience_edit(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=exp)
    return render(request, 'admin_dashboard/experience_form.html', {'form': form, 'title': 'Edit Experience'})

# Messages
@login_required
def message_list(request):
    msgs = ContactMessage.objects.all().order_by('-created_at')
    # Mark as read when viewing
    ContactMessage.objects.all().update(is_read=True)
    return render(request, 'admin_dashboard/messages.html', {'msgs': msgs})

@login_required
def message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    return redirect('message_list')

# About edit
@login_required
def about_edit(request):
    about = About.objects.first()
    if request.method == 'POST':
        if about:
            form = AboutForm(request.POST, request.FILES, instance=about)
        else:
            form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'About information updated!')
            return redirect('dashboard')
    else:
        if about:
            form = AboutForm(instance=about)
        else:
            form = AboutForm()
    return render(request, 'admin_dashboard/about_form.html', {'form': form})




def print_users():
    for user in User.objects.all():
        print(user.username)