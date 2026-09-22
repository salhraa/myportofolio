from django.shortcuts import render
from main.models import Experience, Skill, Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import SkillForm, EducationForm, ExperienceForm


def show_main(request):
    context = {
        "name": "Salma Maharani",
        "npm": "2506586532",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Just a professional daydreamer out here trying every side quest life throws at me. "
            "My entire personality is basically romanticizing the mundane. "
            "Having my mood entirely dictated by whether a stray cat lets me pet it (spoiler: it usually does). "
            "Big on trying new hobbies even if I abandon them two weeks later, but hey, we love a versatile queen. "
            "Listening to music like it's a full-time job, and trying not to let my tech stack or my sleep schedule break down completely. "
            "Pls send cat pics immediately.🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾"

        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salma Maharani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pengalaman baru berhasil ditambahkan!')
            return redirect('main:show_experience')
        else:
            print("Form Errors:", form.errors)
    
    context = {
        'name': 'Salma Maharani',
        'form': form,
        'title': 'Add Experience',
    }
    return render(request, 'experience_form.html', context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Pengalaman berhasil diperbarui!')
        return redirect('main:show_experience')
    
    context = {
        'name': 'Salma Maharani',
        'form': form,
        'title': 'Edit Experience',
    }
    return render(request, 'experience_form.html', context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Pengalaman berhasil dihapus!')
        return redirect('main:show_experience')
    return redirect('main:show_experience')

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
   

def update_skill(request, id):
    skill = get_object_or_404(Skill, pk=id)
    form = SkillForm(request.POST or None, instance=skill)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_skills')

    context = {'form': form}
    return render(request, "skills_form.html", context)

def show_education(request):
    json_response = get_education_json(request)
    education_list = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education_list = [edu.object for edu in education_list]
    
    query = request.GET.get("q", "").strip()
    
    context = {
        "name": "Salma Maharani", 
        "education_list": education_list,
        "query": query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")
    
    context = {
        "name": "Salma Maharani",
        "form": form,
        "title": "Add New Education",
    }
    return render(request, "education_form.html", context)

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan berhasil diperbarui!")
        return redirect("main:show_education")
    
    context = {
        "name": "Salma Maharani",
        "form": form,
        "title": "Edit Education",
    }
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")

def get_education_json(request):
    query = request.GET.get("q", "").strip()
    education_list = Education.objects.all()
    if query:
        education_list = education_list.filter(institution__icontains=query)
    
    education_json = serializers.serialize("json", education_list)
    return HttpResponse(education_json, content_type="application/json")




