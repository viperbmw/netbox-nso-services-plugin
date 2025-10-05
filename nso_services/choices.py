class ServiceTypeChoices:
    SERVICE_TYPE_A = 'service_type_a'
    SERVICE_TYPE_B = 'service_type_b'
    SERVICE_TYPE_C = 'service_type_c'

    CHOICES = [
        (SERVICE_TYPE_A, 'Service Type A'),
        (SERVICE_TYPE_B, 'Service Type B'),
        (SERVICE_TYPE_C, 'Service Type C'),
    ]

class ServiceStatusChoices:
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (PENDING, 'Pending'),
    ]