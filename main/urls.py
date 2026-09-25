from django.urls import path
from main import views
from main.views import create_experience, delete_experience, get_skills_json, login_user, logout_user, register, show_main, show_experience, show_skills, create_skill, delete_skill, show_education, create_education, toggle_star, update_education, delete_education, get_education_json, update_experience, update_skill
create_experience, update_experience, delete_experience, update_skill, register, login_user, logout_user,


app_name = "main"


urlpatterns = [
    path("", show_main, name="show_main"),
    path("skills/add/", create_skill, name="create_skill"),
    path("experience/", show_experience, name="show_experience"),
    path('experience/add/', create_experience, name='create_experience'),
    path('experience/<uuid:experience_id>/edit/', update_experience, name='update_experience'), 
    path('experience/<uuid:experience_id>/delete/', delete_experience, name='delete_experience'),
    path("skills/", show_skills, name="show_skills"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
    path('skills/update/<uuid:id>/', update_skill, name='update_skill'),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:education_id>/edit/", update_education, name="update_education"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("skills/<uuid:skill_id>/star/", toggle_star, name="toggle_star"),
    path('json/', views.get_skills_json, name='get_skills_json'),
]