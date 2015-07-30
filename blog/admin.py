# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Category, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category']
    ordering = ['title']
    actions = ['make_published', 'make_draft', 'make_unpublished']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

    def make_published(self, request, queryset):
        queryset.update(status='1')
    make_published.short_description = "Mark selected stories as published"

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status='2')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as unpublished." % message_bit)
    make_unpublished.short_description = "Mark selected stories as unpublished"

    def make_draft(self, request, queryset):
        queryset.update(status='0')
    make_draft.short_description = "Mark selected stories as draft"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
