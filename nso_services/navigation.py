from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

menu = PluginMenu(
    label='NSO Services',
    groups=(
        ('Services', (
            PluginMenuItem(
                link='plugins:nso_services:nsoservice_list',
                link_text='NSO Services',
                permissions=['nso_services.view_nsoservice']
            ),
            PluginMenuItem(
                link='plugins:nso_services:nsoserviceinstance_list',
                link_text='Service Instances',
                permissions=['nso_services.view_nsoserviceinstance']
            ),
        )),
    ),
)