from django.urls import path

from schema.views import SchemaListView, create_schema, SchemaDetailView, SchemaDeleteView, create_csv, download_csv

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
    path("schema/create/", create_schema, name="schema-create"),
    path("schema/<int:pk>/", SchemaDetailView.as_view(), name="schema-detail"),
    path("schema/<int:pk>/delete/", SchemaDeleteView.as_view(), name="schema-delete"),
    path("schema/<int:pk>/create_csv/", create_csv, name="create-csv"),
]

app_name = "schema"
