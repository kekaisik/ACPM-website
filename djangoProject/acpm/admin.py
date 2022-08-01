from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Post_Images, Event, News, News_Images, Event_Images, User


class PostInLine(admin.StackedInline):
    model = Post_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class EventInLine(admin.StackedInline):
    model = Event_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class NewsInLine(admin.StackedInline):
    model = News_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "tags", "paid", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "tags", "paid", "date", "draft")
    search_fields = ("title", "text", "category", "tags")
    inlines = [PostInLine]
    save_on_top = True
    list_editable = ("paid", "draft")
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        return obj.main_image_preview

    main_image_preview.short_description = "Основное фото"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "paid", "draft")
    list_display_links = ("title",)
    list_filter = ("date", "draft", "paid")
    search_fields = ("title", "text")
    inlines = [EventInLine]
    save_on_top = True
    list_editable = ("paid", "draft")
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        return obj.main_image_preview

    main_image_preview.short_description = "Основное фото"


@admin.register(News)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "paid", "draft")
    list_display_links = ("title",)
    list_filter = ("date", "draft", "paid")
    search_fields = ("title", "text")
    inlines = [NewsInLine]
    save_on_top = True
    list_editable = ("paid", "draft")
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        return obj.main_image_preview

    main_image_preview.short_description = "Основное фото"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)