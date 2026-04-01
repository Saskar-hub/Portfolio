import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_portfolio.settings')
django.setup()

from portfolio.models import Category, SkillCategory, About, Skill, Project, Experience, Education

def seed():
    # 1. About
    if not About.objects.exists():
        About.objects.create(
            name="John Doe",
            title="Full Stack Developer",
            tagline="Building modern web applications with passion and precision.",
            bio="I am a professional full-stack developer with 5+ years of experience in Python, Django, and modern JavaScript. I love solving complex problems and building user-centric products.",
            email="john@example.com",
            location="San Francisco, CA",
            github="https://github.com/",
            linkedin="https://linkedin.com/",
            twitter="https://twitter.com/",
        )
        print("About created.")

    # 2. Categories
    web, _ = Category.objects.get_or_create(name="Web Development", slug="web-dev")
    ai, _ = Category.objects.get_or_create(name="AI & ML", slug="ai-ml")
    mobile, _ = Category.objects.get_or_create(name="Mobile Apps", slug="mobile-apps")
    print("Categories created.")

    # 3. Skill Categories
    frontend, _ = SkillCategory.objects.get_or_create(name="Frontend")
    backend, _ = SkillCategory.objects.get_or_create(name="Backend")
    tools, _ = SkillCategory.objects.get_or_create(name="Tools & Others")
    print("Skill Categories created.")

    # 4. Skills
    Skill.objects.get_or_create(name="HTML5/CSS3", category=frontend, proficiency=95, icon_class="fab fa-html5")
    Skill.objects.get_or_create(name="JavaScript", category=frontend, proficiency=90, icon_class="fab fa-js")
    Skill.objects.get_or_create(name="React", category=frontend, proficiency=85, icon_class="fab fa-react")
    
    Skill.objects.get_or_create(name="Python", category=backend, proficiency=95, icon_class="fab fa-python")
    Skill.objects.get_or_create(name="Django", category=backend, proficiency=90, icon_class="fas fa-server")
    Skill.objects.get_or_create(name="PostgreSQL", category=backend, proficiency=80, icon_class="fas fa-database")
    
    Skill.objects.get_or_create(name="Git", category=tools, proficiency=90, icon_class="fab fa-git-alt")
    Skill.objects.get_or_create(name="Docker", category=tools, proficiency=75, icon_class="fab fa-docker")
    print("Skills created.")

    # 5. Experience
    Experience.objects.get_or_create(
        title="Senior Developer",
        company="Tech Corp",
        duration="Jan 2021 - Present",
        description="Lead developer for the e-commerce platform. Managed a team of 5 developers and improved performance by 40%.",
        is_current=True,
        order=2
    )
    Experience.objects.get_or_create(
        title="Full Stack Developer",
        company="Startup Inc",
        duration="Jun 2018 - Dec 2020",
        description="Developed and maintained several client projects using Django and React.",
        is_current=False,
        order=1
    )
    print("Experience created.")

    # 6. Education
    Education.objects.get_or_create(
        degree="B.S. Computer Science",
        institution="University of Technology",
        duration="2014 - 2018",
        description="Focused on software engineering and database management.",
        order=1
    )
    print("Education created.")

if __name__ == "__main__":
    seed()
