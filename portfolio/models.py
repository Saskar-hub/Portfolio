from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tech_stack = models.CharField(max_length=200) # e.g. "Django, React, PostgreSQL"
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    name = models.CharField(max_length=100) # e.g. "Frontend", "Backend"

    class Meta:
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.IntegerField(default=0) # 0 to 100
    icon_class = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class, e.g., 'fab fa-python'")

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100) # e.g. "Jan 2020 - Present"
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-id']

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-id']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100) # e.g. Full Stack Developer
    tagline = models.TextField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='about/')
    resume = models.FileField(upload_to='resume/')
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.name

