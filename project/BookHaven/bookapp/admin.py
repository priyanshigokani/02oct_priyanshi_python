from django.contrib import admin
from .models import *


# Register your models here.

class bookdata(admin.ModelAdmin):
    list_display=['auname','booktitle','pdate','genre']

admin.site.register(Book,bookdata)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_approved')  # Show columns in admin
    list_filter = ('is_approved',)  # Add filter for approval
    actions = ['approve_authors', 'reject_authors']  # Custom actions

    def approve_authors(self, request, queryset):
        queryset.update(STATUS_CHOICES='Approved')
    approve_authors.short_description = "Approve selected authors"

    def reject_authors(self, request, queryset):
        queryset.update(STATUS_CHOICES='Rejected')
    reject_authors.short_description = "Reject selected authors"

admin.site.register(Author, AuthorAdmin)

