from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.index.models import IndexInSubInf
from applications.index.models import YanGooAnalytics


class IndexInSubInfAdminForm(forms.ModelForm):
    class Meta:
        model = IndexInSubInf
        fields = "__all__"
        widgets = {"ist": forms.Textarea()}


@admin.register(IndexInSubInf)
class IndexInSubInfAdminModel(ModelAdmin):
    form = IndexInSubInfAdminForm


class CodeMetrikaAdminForm(forms.ModelForm):
    class Meta:
        model = YanGooAnalytics
        fields = "__all__"
        widgets = {"type_metrika": forms.Textarea(),
                   "code_metrika": forms.Textarea()}


@admin.register(YanGooAnalytics)
class YanGooAnalyticsAdminModel(ModelAdmin):
    form = CodeMetrikaAdminForm
