from django.urls import path

from schema.views import SchemaListView, create_schema, SchemaDetailView

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
    path("schema/create/", create_schema, name="schema-create"),
    path("schema/<int:pk>/", SchemaDetailView.as_view(), name="schema-detail"),
]

app_name = "schema"
