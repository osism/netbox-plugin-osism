from django.core.exceptions import ObjectDoesNotExist

from extras.plugins import PluginTemplateExtension


class InterfacesOSISM(PluginTemplateExtension):
    model = "dcim.device"

    def right_page(self):
        template_filename = "netbox_plugin_osism/interfaces.html"

        try:
            return self.render(
                template_filename,
                extra_context={
                    'device': self.context['object'],
                    'grafana': self.context['config'].get('grafana'),
                    'netdata': self.context['config'].get('netdata')
                }
            )
        except ObjectDoesNotExist:
            return ""


template_extensions = [InterfacesOSISM]
