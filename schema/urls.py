from django.urls import path

from schema.views import SchemaListView, create_schema

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
    path("schema/create/", create_schema, name="schema-create"),
]

app_name = "schema"
