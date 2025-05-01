from django.contrib import admin

from .models import WaksKevin


@admin.register(WaksKevin)
class WaksKevinAdmin(admin.ModelAdmin):
    exclude = ("manifest",)

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
