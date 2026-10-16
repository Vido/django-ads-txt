try:
    from import_export.admin import ImportExportModelAdmin as SuperModelAdmin
except ImportError:
    from django.contrib.admin import ModelAdmin as SuperModelAdmin
from django.contrib.admin import register
from .models import Rule, AppRule

@register(Rule)
class RuleAdmin(SuperModelAdmin):
    list_display = ['domain', 'account_id', 'account_type', 'authority_id']
    base_change_list_template = SuperModelAdmin.change_list_template or 'admin/change_list.html'
    change_list_template = 'ads_txt/admin/ads_txt/adstxt/change_list.html'
    bulk_upload_url_name = 'ads_txt_bulk_upload'

    def changelist_view(self, request, extra_context=None):
        extra_context = dict(extra_context or {},
                             base_change_list_template=self.base_change_list_template,
                             bulk_upload_url_name=self.bulk_upload_url_name)
        return super().changelist_view(request, extra_context)


@register(AppRule)
class AppRuleAdmin(RuleAdmin):
    bulk_upload_url_name = 'ads_txt_app_bulk_upload'
