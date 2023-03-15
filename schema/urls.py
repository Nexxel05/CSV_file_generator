from django.urls import path

from schema.views import SchemaListView

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema-list"),
]

app_name = "schema"
