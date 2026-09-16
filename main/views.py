from django.shortcuts import render
from main.models import Experience, Skill
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import SkillForm

def show_main(request):
    context = {
        "name": "Salma Maharani",
        "npm": "2506586532",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan kesenian."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salma Maharani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    json_response = get_skills_json(request)
    skills = serializers.deserialize(
       "json",
       json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    title_query = request.GET.get("title", "").strip()
    if title_query:
        skills: [
            skill for skill in skills
            if title_query.lower() in skill.name.lower()
        ] # type: ignore
    context = {
        "name": "Salma Maharani",
        "skill_list" : skills,
        "title_query": title_query,
    }
    return render(request, "skill.html", context)

def create_skill(request):
  form = SkillForm(request.POST or None)

  if request.method == "POST" and form.is_valid():
    form.save()
    messages.success(request, "Skill baru berhasil ditambahkan!")
    return redirect("main:show_skills") 
  context = {
      "name": "Salma Maharani", 
      "form": form,
  }

  return render(request, "skills_form.html", context)

def get_skills_json(request):
    title_query = request.GET.get("title", "").strip()
    skills = Skill.objects.all()

    if title_query:
        skills = skills.filter(name__icontains=title_query)

    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")

def delete_skill(request, skill_id):
   skill = get_object_or_404(Skill, pk=skill_id)
   if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")