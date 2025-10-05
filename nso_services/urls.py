from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = [
    # NSO Services
    path('services/', views.ServiceListView.as_view(), name='nsoservice_list'),
    path('services/add/', views.ServiceEditView.as_view(), name='nsoservice_add'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='nsoservice'),
    path('services/<int:pk>/edit/', views.ServiceEditView.as_view(), name='nsoservice_edit'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='nsoservice_delete'),
    path('services/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nsoservice_changelog', kwargs={'model': models.NSOService}),

    # NSO Service Instances
    path('instances/', views.ServiceInstanceListView.as_view(), name='nsoserviceinstance_list'),
    path('instances/add/', views.ServiceInstanceEditView.as_view(), name='nsoserviceinstance_add'),
    path('instances/allocate/', views.allocate_instance, name='nsoserviceinstance_allocate'),
    path('instances/<int:pk>/', views.ServiceInstanceDetailView.as_view(), name='nsoserviceinstance'),
    path('instances/<int:pk>/edit/', views.ServiceInstanceEditView.as_view(), name='nsoserviceinstance_edit'),
    path('instances/<int:pk>/delete/', views.ServiceInstanceDeleteView.as_view(), name='nsoserviceinstance_delete'),
    path('instances/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nsoserviceinstance_changelog', kwargs={'model': models.NSOServiceInstance}),
]