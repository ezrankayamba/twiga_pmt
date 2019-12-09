from import_export import resources
from . import models
from django.db.models import F
from import_export import fields, resources
from import_export import widgets


class ProjectResource(resources.ModelResource):
    name = fields.Field(column_name='Name', attribute='name')
    type = fields.Field(column_name='Type', attribute='type')
    start_date = fields.Field(column_name='Start Date', attribute='start_date', widget=widgets.DateWidget(format='%d/%m/%Y'))
    status = fields.Field(column_name='Status', attribute='get_status')
    region__name = fields.Field(column_name='Region', attribute='region__name')
    district__name = fields.Field(column_name='District', attribute='district__name')
    town = fields.Field(column_name='Town', attribute='town')
    duration = fields.Field(column_name='Duration (Yrs)', attribute='duration')
    authority__name = fields.Field(column_name='Authority', attribute='authority__name')
    consultant__name = fields.Field(column_name='Consultant', attribute='consultant__name')
    quantity_demanded = fields.Field(column_name="Qty Demanded (Tons)", attribute='quantity_demanded')
    quantity_supplied = fields.Field(column_name="Qty Supplied (Tons)", attribute='quantity_supplied')
    longitude = fields.Field(column_name="Longitude", attribute="longitude")
    latitude = fields.Field(column_name="Latitude", attribute="latitude")
    remarks = fields.Field(column_name="Remarks", attribute="remarks")

    def __init__(self, user):
        self.user = user

    class Meta:
        model = models.Project
        fields = ['name', 'type', 'start_date', 'status', 'region__name', 'district__name', 'town', 'duration', 'authority__name', 'consultant__name', 'quantity_demanded', 'quantity_supplied', 'latitude', 'longitude', 'remarks']
        export_order = fields

    def get_queryset(self):
        return models.Project.objects.all().order_by('-date_created')
