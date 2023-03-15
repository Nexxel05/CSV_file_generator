from django.urls import path

from schema.views import SchemaListView, create_schema, SchemaDetailView, SchemaDeleteView

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
    path("schema/create/", create_schema, name="schema-create"),
    path("schema/<int:pk>/", SchemaDetailView.as_view(), name="schema-detail"),
    path("schema/<int:pk>/delete/", SchemaDeleteView.as_view(), name="schema-delete"),
]

app_name = "schema"
