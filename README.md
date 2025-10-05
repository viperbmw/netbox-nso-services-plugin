# NetBox NSO Services Plugin

A NetBox plugin for tracking and managing Cisco NSO (Network Services Orchestrator) services and their instances within your network infrastructure.

## Features

- **NSO Service Management**: Track NSO services with status, regions, and Git repository links
- **Service Instances**: Create and manage instances of NSO services
- **Device Integration**: Associate service instances with specific devices or device roles
- **JSON Configuration Storage**: Store service-specific JSON configuration data
- **API Extensions**: Automatically extends NetBox's Device API to include NSO service instance information
- **Device Tab Integration**: Adds a dedicated tab to device detail pages showing associated NSO services

## Requirements

- NetBox 3.x or later
- Python 3.8+

## Installation

1. Install the plugin:
   ```bash
   pip install git+https://github.com/viperbmw/netbox-nso-services-plugin.git
   ```

2. Add the plugin to your NetBox `configuration.py`:
   ```python
   PLUGINS = [
       'nso_services',
   ]
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Restart NetBox services:
   ```bash
   systemctl restart netbox netbox-rq
   ```

## Usage

### Creating NSO Services

1. Navigate to **Plugins > NSO Services** in the NetBox UI
2. Click **Add** to create a new NSO service
3. Fill in the service details:
   - **Name**: Unique identifier for the service
   - **Description**: Optional description
   - **Status**: Service status (Active, Planned, etc.)
   - **Region**: Associated region
   - **Git Repository URL**: Link to the service's Git repository
   - **JSON Body**: Service-specific configuration data

### Creating Service Instances

1. From an NSO Service detail page, create instances
2. Configure the instance:
   - **Name**: Instance identifier
   - **Status**: Instance status
   - **Region**: Associated region
   - **Devices**: Specific devices using this instance
   - **Device Roles**: Device roles that should use this instance
   - **JSON Body**: Instance-specific configuration data

### API Usage

The plugin extends NetBox's REST API with the following endpoints:

```bash
# List all NSO services
GET /api/plugins/nso-services/services/

# Get a specific service
GET /api/plugins/nso-services/services/{id}/

# List all service instances
GET /api/plugins/nso-services/instances/

# Get a specific instance
GET /api/plugins/nso-services/instances/{id}/
```

Device API responses are automatically extended to include `nso_service_instances`:

```bash
GET /api/dcim/devices/{id}/
```

## Models

### NSOService

- `name`: Service name (unique)
- `description`: Optional description
- `status`: Service status
- `region`: Associated NetBox region
- `git_repo_url`: Git repository URL
- `json_body`: JSON configuration data

### NSOServiceInstance

- `service`: Foreign key to NSOService
- `name`: Instance name
- `status`: Instance status
- `region`: Associated NetBox region
- `devices`: Many-to-many relationship with NetBox devices
- `device_roles`: Many-to-many relationship with device roles
- `json_body`: JSON configuration data

## Development

To set up a development environment:

```bash
git clone https://github.com/viperbmw/netbox-nso-services-plugin.git
cd netbox-nso-services-plugin
pip install -e .
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

**cwd** - [casey@cwdavis.net](mailto:casey@cwdavis.net)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
