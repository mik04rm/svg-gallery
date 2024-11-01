from django.contrib import admin

from .models import Tag, Image
# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'width', 'height')
#     filter_horizontal = ('artists',)  # This adds the many-to-many relationship widget

# admin.site.register(Image, ImageAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'width', 'height')
    list_filter = ('tags', 'pub_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags', 'artists',)  # ManyToManyField easier to manage

