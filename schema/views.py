from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from schema.forms import SchemaCreationForm
from schema.models import Schema


class SchemaListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Schema
    queryset = Schema.objects.all()


def create_schema(request):
    schema_form = SchemaCreationForm(request.POST or None, user=request.user)

    context = {
        "schema_form": schema_form
    }

    if schema_form.is_valid():
        schema_form.save()
        return HttpResponseRedirect(reverse("schema:schema-list"))

    return render(request, "schema/schema_form.html", context=context)
