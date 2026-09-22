from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput
from main.models import Skill, Education, Experience
from django import forms


class SkillForm(ModelForm):

  class Meta:
    model = Skill
    fields = ["name", "level", "description", "skill_image_url"]
    labels = {
        "name": "Skill Name",
        "level": "Proficiency Level",
        "description": "Skill Description",
    }
    widgets = {
        "name": TextInput(
            attrs={
                "placeholder": "Input skill name",
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
                "placeholder": "explain your experience or understanding about this skill...",
                "rows": 3,
            }
        ),
        'skill_image_url': forms.URLInput(attrs={
                'class': 'skill-search__input', 
                'placeholder': 'Image link'
            }),
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
            "institution": "Institution Nmae",
            "degree": "Degree / Academic Level",
            "field_of_study": "Field of Study",
            "start_year": "Enrollment Year",
            "end_year": "Graduation Year",
            "description": "Description",
        }
        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "example: Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "example: Bachelor's Degree",
                    "maxlength": 100,
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "example: Information System",
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
                    "placeholder": "tell about your study focus...",
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