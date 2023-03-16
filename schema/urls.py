from django.urls import path

from schema.views import (
    SchemaListView,
    create_schema,
    SchemaDetailView,
    SchemaDeleteView,
    create_csv,
    download_csv,
    update_schema
)

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
    path("schema/create/", create_schema, name="schema-create"),
    path("schema/<int:pk>/", SchemaDetailView.as_view(), name="schema-detail"),
    path("schema/<int:pk>/update/", update_schema, name="schema-update"),
    path("schema/<int:pk>/delete/", SchemaDeleteView.as_view(), name="schema-delete"),
    path("schema/<int:pk>/create_csv/", create_csv, name="create-csv"),
    path("schema/dataset/<int:pk>/download_csv/", download_csv, name="download-csv"),
]

app_name = "schema"
