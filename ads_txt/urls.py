from django.urls import re_path
from ads_txt.views import rules_list, app_rules_list

urlpatterns = [
    re_path(r'^ads\.txt$', rules_list, name='ads_txt_rule_list'),
    re_path(r'^app-ads\.txt$', app_rules_list, name='ads_txt_app_rule_list'),
]
