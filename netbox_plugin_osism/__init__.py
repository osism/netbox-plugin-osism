from extras.plugins import PluginConfig
from .version import __version__


class OSISMConfig(PluginConfig):
    name = 'netbox_plugin_osism'
    verbose_name = 'OSISM'
    description = 'OSISM integration'
    version = __version__
    author = 'OSISM GmbH'
    author_email = 'info@osism.tech'
    base_url = 'osism'
    required_settings = []
    min_version = '3.2.0'
    max_version = '3.2.99'
    default_settings = {
        'grafana': 'http://localhost:3000',
        'netdata': 'http://localhost:19999'
    }


config = OSISMConfig # noqa
