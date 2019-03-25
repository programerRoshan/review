from django.contrib import admin

from .models import Review
# Register your models here
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'Faculty', 'timeStamp']
    class Meta:
        model = Review

admin.site.register(Review, ReviewAdmin)
