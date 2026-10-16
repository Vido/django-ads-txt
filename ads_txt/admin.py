try:
    from import_export.admin import ImportExportModelAdmin as SuperModelAdmin
except ImportError:
    from django.contrib.admin import ModelAdmin as SuperModelAdmin
from django.contrib.admin import register
from django.urls import path, reverse_lazy
from .models import Rule, AppRule
from .views import UploadRulesFormView

@register(Rule, AppRule)
class RuleAdmin(SuperModelAdmin):
    list_display = ['domain', 'account_id', 'account_type', 'authority_id']
    change_list_template = 'ads_txt/admin/ads_txt/adstxt/change_list.html'

    def get_urls(self):
        info = self.admin_site.name, self.model._meta.app_label, self.model._meta.model_name
        upload = UploadRulesFormView.as_view(model=self.model, success_url=reverse_lazy('%s:%s_%s_changelist' % info))
        return [path('bulk_upload/', self.admin_site.admin_view(upload), name='%s_%s_bulk_upload' % info[1:])] + super().get_urls()

    def changelist_view(self, request, extra_context=None):
        base = super().change_list_template or 'admin/change_list.html'
        return super().changelist_view(request, dict(extra_context or {}, base_change_list_template=base))
