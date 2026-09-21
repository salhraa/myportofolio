from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput
from main.models import Skill, Education, Experience
from django import forms


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

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "field_of_study",
            "start_year",
            "end_year",
            "description",
        ]
        labels = {
            "institution": "Nama Instansi / Universitas",
            "degree": "Gelar / Jenjang",
            "field_of_study": "Bidang Studi",
            "start_year": "Tahun Masuk",
            "end_year": "Tahun Lulus (Kosongkan jika masih berjalan)",
            "description": "Deskripsi / Kegiatan",
        }
        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Contoh: Sarjana (S1)",
                    "maxlength": 100,
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "Contoh: Sistem Informasi",
                    "maxlength": 100,
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2029",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan fokus studi atau pencapaianmu...",
                    "rows": 3,
                }
            ),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'description', 'started_at', 'ended_at']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid #444; background: #fff; color: #000;'}),
            'category': forms.Select(attrs={'style': 'width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid #444; background: #fff; color: #000;'}),
            'description': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid #444; background: #fff; color: #000;'}),
            'started_at': forms.DateInput(attrs={'type': 'date', 'style': 'width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid #444; background: #fff; color: #000;'}),
            'ended_at': forms.DateInput(attrs={'type': 'date', 'style': 'width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid #444; background: #fff; color: #000;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'started_at' in self.fields:
            self.fields['started_at'].required = True
        if 'ended_at' in self.fields:
            self.fields['ended_at'].required = False