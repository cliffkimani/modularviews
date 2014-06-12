from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from lt.django.company.models import CompanyPlugin
from django.utils.translation import ugettext as _

class CMSCompanyPlugin(CMSPluginBase):
        model = CompanyPlugin
        name = _("Company")
        render_template = "company/company.html"
        
        def render(self, context, instance, placeholder):
            context.update({'instance':instance,
                            'placeholder': placeholder})
            return context

plugin_pool.register_plugin(CMSCompanyPlugin)
