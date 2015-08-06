# -*- coding:utf-8 -*-
from django import forms
from django.contrib import admin
from blog.models import Category, Post
from ckeditor.widgets import CKEditorWidget
from blog.models import UserProfile

# Register your models here.
class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Post
        fields = "__all__"

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category']
    ordering = ['title']
    actions = ['make_published', 'make_draft', 'make_unpublished']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    form = PostAdminForm

    def make_published(self, request, queryset):
        #queryset.update(status='1')
        rows_published = queryset.update(status='1')
        if rows_published == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_published
        self.message_user(request, "%s successfully marked as published." % message_bit)
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
        #queryset.update(status='0')
        rows_drafted = queryset.update(status='0')
        if rows_drafted == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_drafted
        self.message_user(request, "%s successfully marked as draft." % message_bit)
    make_draft.short_description = "Mark selected stories as draft"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
