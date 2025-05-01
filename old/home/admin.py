from django.contrib import admin

from .models import Fact, Hero, Resume, Skill


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 10: # 10 skills max
            return False
        return True


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
