from django import forms
from django.db import models
from django.contrib import admin
from markitup.demo.models import Newsletter
from markitup.demo.widgets import MarkItUpEditor

class NewsletterAdminForm(forms.ModelForm):
    class Meta:
        model = Newsletter
    
    plainText = forms.CharField(widget = forms.Textarea())
    html = forms.CharField(widget = MarkItUpEditor())

class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterAdminForm
    
admin.site.register(Newsletter, NewsletterAdmin)