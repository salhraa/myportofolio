from django.urls import path

from main.views import get_skills_json, show_main, show_experience, show_skills, create_skill, delete_skill


app_name = "main"


urlpatterns = [
    path("", show_main, name="show_main"),
    path("skills/add/", create_skill, name="create_skill"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
]