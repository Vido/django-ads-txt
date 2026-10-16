from django.conf.urls import url
from ads_txt.views import rules_list, app_rules_list, bulk_upload_rules, bulk_upload_app_rules

urlpatterns = [
    url(r'^ads\.txt$', rules_list, name='ads_txt_rule_list'),
    url(r'^app-ads\.txt$', app_rules_list, name='ads_txt_app_rule_list'),
    url(r'^ads_txt/upload$', bulk_upload_rules, name='ads_txt_bulk_upload'),
    url(r'^ads_txt/app/upload$', bulk_upload_app_rules, name='ads_txt_app_bulk_upload'),
]
