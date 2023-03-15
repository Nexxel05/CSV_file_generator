from django.shortcuts import render
from django.views import generic

from schema.models import Schema


class SchemaListView(generic.ListView):
    model = Schema
    queryset = Schema.objects.all()
