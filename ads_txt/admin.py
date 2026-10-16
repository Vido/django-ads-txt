try:
    from import_export.admin import ImportExportModelAdmin as SuperModelAdmin
except ImportError:
    from django.contrib.admin import ModelAdmin as SuperModelAdmin
from django.contrib.admin import register
from .models import Rule

@register(Rule)
class RuleAdmin(SuperModelAdmin):
    list_display = ['domain', 'account_id', 'account_type', 'authority_id']
