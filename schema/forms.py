from django import forms

from schema.models import Schema, Column


class SchemaCreationForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ("title",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(SchemaCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        schema = super(SchemaCreationForm, self).save(commit=False)
        schema.user = self.user
        schema.save()
        return schema


class ColumnCreationForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = "__all__"
