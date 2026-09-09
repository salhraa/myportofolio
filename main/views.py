from django.shortcuts import render

from main.models import Experience


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