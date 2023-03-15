from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from schema.models import Schema


class SchemaListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Schema
    queryset = Schema.objects.all()
