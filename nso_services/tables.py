import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import NSOService, NSOServiceInstance

class ServiceTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = columns.ChoiceFieldColumn()
    region = tables.Column(
        linkify=True
    )
    git_repo_url = tables.URLColumn(
        verbose_name='Git Repository',
        text='View Repo'
    )
    tags = columns.TagColumn(
        url_name='plugins:nso_services:nsoservice_list'
    )

    class Meta(NetBoxTable.Meta):
        model = NSOService
        fields = ('pk', 'id', 'name', 'status', 'region', 'git_repo_url', 'description', 'tags')
        default_columns = ('name', 'status', 'region', 'git_repo_url', 'tags')


class ServiceInstanceTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    service = tables.Column(
        linkify=True
    )
    status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn(
        url_name='plugins:nso_services:nsoserviceinstance_list'
    )

    class Meta(NetBoxTable.Meta):
        model = NSOServiceInstance
        fields = ('pk', 'id', 'name', 'service', 'status', 'tags')
        default_columns = ('name', 'service', 'status', 'tags')