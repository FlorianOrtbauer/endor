from django.db import models
import uuid
from django.urls import reverse
from django.utils.timezone import now

class Client(models.Model):
    """Model representing a Client."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a client')
    name = models.CharField(max_length=50, help_text='Enter the name of your organisation')
    priority = models.IntegerField(help_text='Enter client priority. 0 = low')
    country = models.CharField(max_length=3, help_text='3 digit country code')
    address_line_1 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_2 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_3 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_4 = models.CharField(max_length=50, help_text='Enter address information here')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['country']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a site')
    client_id = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, help_text='Enter the name of your site')
    priority = models.IntegerField(help_text='Enter site priority. 0 = low')
    country = models.CharField(max_length=3, help_text='3 digit country code')
    address_line_1 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_2 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_3 = models.CharField(max_length=50, help_text='Enter address information here')
    address_line_4 = models.CharField(max_length=50, help_text='Enter address information here')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['country']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for an area')
    site_id = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, help_text='Enter the area name')
    priority = models.IntegerField(help_text='Enter area priority. 0 = low')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['site_id']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class System(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a system')
    area_id = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, help_text='Enter the system name')
    priority = models.IntegerField(help_text='Enter system priority. 0 = low')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['area_id']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Component(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a component')
    system_id = models.ForeignKey('System', on_delete=models.SET_NULL, null=True)
    #supplier_id ToDo: add entity Supplier
    name = models.CharField(max_length=50, help_text='Enter the component name')
    priority = models.IntegerField(help_text='Enter component priority. 0 = low')
    golive = models.DateTimeField(help_text='Enter first usage of the component')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['system_id']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Mission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a mission')
    component_id = models.ForeignKey('Component', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, help_text='Enter the mission name')
    priority = models.IntegerField(help_text='Enter mission priority. 0 = low')
    short_desc = models.CharField(max_length=200, help_text='Enter short description of the mission')
    instruction = models.TextField(max_length=1000, help_text='Enter detailed instructions for the mission')
    
    MISSION_TYPE = (
        ('p', 'PPM'),
        ('r', 'REPAIR'),
        ('c', 'CHECK'),
    )
    mission_type = models.CharField(
        max_length=1,
        choices = MISSION_TYPE,
        blank=True,
        default='c',
        help_text='Mission type')
    
    MISSION_STATUS = (
        ('i', 'IDLE'),
        ('a', 'ACTIVE'),
        ('p', 'PAUSED'),
    )
    status = models.CharField(
        max_length=1,
        choices = MISSION_TYPE,
        blank=True,
        default='i',
        help_text='Mission status')

    last_execution = models.DateTimeField(help_text='Enter last execution date')
    last_duration = models.CharField(max_length=10, help_text='Enter last duration')
    planned_duration = models.CharField(max_length=10, help_text='Enter planned duration')
    execution_interval = models.IntegerField(help_text='mission execution interval')
    next_due = models.DateTimeField(default = now, help_text='Enter (calculate) next due date')
    KPI_reference = models.CharField(max_length=10, help_text='Enter KPI')
    dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
    ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
    dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
    ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

    class Meta:
        ordering = ['component_id', 'status']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    
    class Task(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Task')
        mission_id = models.ForeignKey('Mission', on_delete=models.SET_NULL, null=True)
        assigned_user = models.CharField(max_length=50, help_text='Assigned User')  #ToDo: this one needs to be lined to user management
        
        TASK_STATUS = (
            ('c', 'CREATED'),
            ('p', 'PLANNED'),
            ('a', 'ACTIVE'),
            ('f', 'FINISHED'),
            ('d', 'DEFERRED'),
        )
        status = models.CharField(
            max_length=1,
            choices = TASK_STATUS,
            blank=True,
            default='i',
            help_text='Mission status',
        )

        planned_start = models.DateTimeField(default = now, help_text='Planned time of task execution')
        act_start = models.DateTimeField(default = now, help_text='Task beginning timestamp')
        act_end = models.DateTimeField(default = now, help_text='Task ending timestamp')
        comment = models.CharField(max_length=50, help_text='Engineers comment') 
        dcr = models.DateTimeField(auto_now_add=True, help_text='Creation date')
        ucr = models.CharField(max_length=50, help_text='Creation user') #ToDo: this one needs to be lined to user management
        dlm = models.DateTimeField(auto_now=True, help_text='Last modification date')
        ulm = models.CharField(max_length=50, help_text='Last modification user') #ToDo: this one needs to be lined to user management

        class Meta:
            ordering = ['status']

        def __str__(self):
            """String for representing the Model object."""
            return self.id


