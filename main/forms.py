from django.forms import ModelForm, Select, TextInput, Textarea
from main.models import Skill


class SkillForm(ModelForm):

  class Meta:
    model = Skill
    fields = ["name", "level", "description"]
    labels = {
        "name": "Nama Skill",
        "level": "Tingkat Keahlian",
        "description": "Deskripsi Skill",
    }
    widgets = {
        "name": TextInput(
            attrs={
                "placeholder": "Contoh: Python, Digital Logic, AVR Assembly",
                "maxlength": 100,
            }
        ),
        "level": Select(
            attrs={
                "class": "form-select", 
            }
        ),
        "description": Textarea(
            attrs={
                "placeholder": "Jelaskan pengalaman atau pemahamanmu tentang skill ini...",
                "rows": 3,
            }
        ),
    }

from main.models import Artwork, Skill

