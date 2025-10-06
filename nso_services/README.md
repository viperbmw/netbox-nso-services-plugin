# NSO Services Plugin

NetBox plugin for tracking and managing Cisco NSO (Network Services Orchestrator) services and their instances.

## Plugin Features

### Data Models

**NSOService** - Represents an NSO service type/template
- Name (unique identifier)
- Description
- Status (Active, Planned, Staged, Decommissioning, Retired)
- Region assignment
- Git repository URL
- JSON configuration body

**NSOServiceInstance** - Deployed instance of an NSO service
- Parent service reference
- Instance name
- Status
- Region assignment
- Device associations (many-to-many)
- Device role associations (many-to-many)
- JSON configuration body

### Web UI Features

**Navigation Menu**
- Access via Plugins > NSO Services
- List views for services and instances
- Detail, create, edit, and delete views

**Device Integration**
- Service instances displayed on device detail pages
- Shows instances assigned directly to device or via device role
- Template extension adds service information to device views

**Device Role Integration**
- Service instances displayed on device role pages
- Shows all instances assigned to that role

### REST API

**Endpoints**
- `/api/plugins/nso-services/services/` - NSO services CRUD
- `/api/plugins/nso-services/instances/` - Service instances CRUD

**Device API Extension**
- Extends `/api/dcim/devices/{id}/` responses
- Adds `nso_service_instances` field with related instances

### Forms and Filters

**Forms**
- ServiceForm - Create/edit NSO services
- ServiceInstanceForm - Create/edit service instances
- ServiceInstanceAllocationForm - Allocate instances to devices/roles

**Filters**
- Filter services by name, status, region
- Filter instances by service, status, region, devices, device roles

### Template Extensions

**DeviceNSOServices**
- Displays service instances on device detail pages
- Shows instances where device is directly assigned OR device role matches

**DeviceRoleNSOServices**
- Displays service instances on device role pages
- Shows all instances assigned to the role

## Module Structure

```
nso_services/
├── __init__.py                 # Plugin configuration
├── models.py                   # Data models (NSOService, NSOServiceInstance)
├── views.py                    # Web UI views
├── forms.py                    # Django forms
├── forms_extensions.py         # Form extensions
├── tables.py                   # Table definitions for list views
├── filtersets.py               # Filtering logic
├── urls.py                     # URL routing
├── navigation.py               # Plugin menu structure
├── search.py                   # Search integration
├── choices.py                  # Choice field definitions
├── template_content.py         # Template extensions for devices
├── api_extensions.py           # Device API serializer extensions
├── api/
│   ├── serializers.py          # REST API serializers
│   ├── nested_serializers.py  # Nested serializers for related objects
│   ├── views.py                # API viewsets
│   └── urls.py                 # API URL routing
├── templatetags/
│   └── nso_extras.py           # Custom template tags
└── migrations/                 # Database migrations
```

## Usage Examples

### Creating a Service via API

```python
import requests

response = requests.post(
    'https://netbox.example.com/api/plugins/nso-services/services/',
    headers={'Authorization': 'Token YOUR_TOKEN'},
    json={
        'name': 'L3VPN-Service',
        'description': 'Layer 3 VPN service',
        'status': 'active',
        'git_repo_url': 'https://github.com/example/l3vpn-service',
        'json_body': {'version': '1.0', 'type': 'vpn'}
    }
)
```

### Creating an Instance via API

```python
response = requests.post(
    'https://netbox.example.com/api/plugins/nso-services/instances/',
    headers={'Authorization': 'Token YOUR_TOKEN'},
    json={
        'service': 1,
        'name': 'customer-abc-vpn',
        'status': 'active',
        'region': 2,
        'devices': [10, 11, 12],
        'json_body': {'customer_id': 'ABC-123', 'vlan': 100}
    }
)
```

### Querying Device Service Instances

```python
# Get device with extended service instance data
response = requests.get(
    'https://netbox.example.com/api/dcim/devices/10/',
    headers={'Authorization': 'Token YOUR_TOKEN'}
)

# Response includes nso_service_instances field
service_instances = response.json()['nso_service_instances']
```

### Filtering Instances

```python
# Get all instances for a specific service
response = requests.get(
    'https://netbox.example.com/api/plugins/nso-services/instances/?service_id=1',
    headers={'Authorization': 'Token YOUR_TOKEN'}
)

# Get instances in a specific region
response = requests.get(
    'https://netbox.example.com/api/plugins/nso-services/instances/?region_id=2',
    headers={'Authorization': 'Token YOUR_TOKEN'}
)
```

## Configuration

The plugin is configured in `__init__.py`:

```python
class NSOServicesConfig(PluginConfig):
    name = 'nso_services'
    verbose_name = 'NSO Services'
    description = 'Track Cisco NSO services within NetBox'
    version = '0.1'
    base_url = 'nso-services'
```

No additional settings required - the plugin works out of the box after installation and migration.
