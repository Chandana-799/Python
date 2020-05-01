from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Tutorial , TutorialSeries, TutorialCategory
from django.db import models

class Tutorial1(admin.ModelAdmin):
    fieldsets = [
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
        ("URL", {"fields": ["tutorial_slug"]}),
        ("Series", {"fields": ["tutorial_series"]}),
        ("content",{"fields":["tutorial_content"]})
]

    formfield_overrides = {
        models.TextField:{"widget":TinyMCE()}
    }

admin.site.register(Tutorial, Tutorial1)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
