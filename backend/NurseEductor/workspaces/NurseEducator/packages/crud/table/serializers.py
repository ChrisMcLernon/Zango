import pytz

from django.db import models
from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass

from zelthy.core.utils import get_current_request
from zelthy.core.storage_utils import ZFileField
from zelthy.apps.dynamic_models.fields import ZForeignKey, ZOneToOneField


class StringRelatedMeta(SerializerMetaclass):
    def __new__(cls, name, bases, attrs):
        # Get the Meta class from attrs
        meta = attrs.get("Meta", None)
        metadata = attrs.get("metadata", {})
        # Check if there's a model defined in Meta
        tenant = get_current_request().tenant
        if meta and hasattr(meta, "model"):
            model = meta.model
            # Iterate through the model's fields
            # fields = attrs['Meta'].__dict__.get('fields')
            # if fields == '__all__':
            #     fields = model._meta
            fields = getattr(meta, "fields", model._meta.fields)
            for field in fields:
                # Check if the field is a relational field
                if isinstance(
                    field,
                    (
                        models.ForeignKey,
                        models.OneToOneField,
                        ZForeignKey,
                        ZOneToOneField,
                    ),
                ):
                    # Use StringRelatedField for this field
                    related_object_attribute = None
                    for column in metadata["columns"]:
                        if column["name"] == field.name:
                            if column.get("related_object_attribute"):
                                related_object_attribute = column[
                                    "related_object_attribute"
                                ]
                    if related_object_attribute is not None:
                        attrs[field.name] = ForeignKeySerializer(
                            related_object_attribute
                        )
                    else:
                        attrs[field.name] = serializers.StringRelatedField()
                if isinstance(field, (models.DateTimeField)):
                    attrs[field.name] = serializers.DateTimeField(
                        format=tenant.datetime_format,
                        default_timezone=pytz.timezone(tenant.timezone),
                    )
                if isinstance(field, (models.FileField, ZFileField)):
                    attrs[field.name] = FileSerializer()

        return super().__new__(cls, name, bases, attrs)


from zelthy.apps.appauth.models import UserRoleModel


class TestSerializer(serializers.ModelSerializer, metaclass=StringRelatedMeta):
    class Meta:
        model = UserRoleModel


class FileSerializer(serializers.Field):
    def to_representation(self, value):
        if not value:
            return "NA"
        request = get_current_request()
        url = request.build_absolute_uri(value.url)
        svg = f"""
            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 50 50">
                <a xlink:href='{url}' target='_blank'> 
                    <path d="M24.707,8.793l-6.5-6.5C18.019,2.105,17.765,2,17.5,2H7C5.895,2,5,2.895,5,4v22c0,1.105,0.895,2,2,2h16c1.105,0,2-0.895,2-2 V9.5C25,9.235,24.895,8.981,24.707,8.793z M18,10c-0.552,0-1-0.448-1-1V3.904L23.096,10H18z"></path>
                </a>
            </svg>
            """
        return svg


class ForeignKeySerializer(serializers.Field):
    def __init__(self, field, *args, **kwargs):
        super(ForeignKeySerializer, self).__init__(*args, **kwargs)
        self.field = field

    def to_representation(self, value):
        return vars(value).get(self.field)
