from django.contrib import admin
from .models import Post, PostPicture


class PostPictureInline(admin.TabularInline):
    model = PostPicture
    extra = 1


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('author', '__str__', 'created')
    inlines = [PostPictureInline,]


admin.site.register(Post, PostAdmin)
