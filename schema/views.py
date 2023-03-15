from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from schema.forms import SchemaCreationForm, ColumnCreationForm
from schema.models import Schema, Column


class SchemaListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Schema
    queryset = Schema.objects.all()


def create_schema(request):
    schema_form = SchemaCreationForm(request.POST or None, user=request.user)
    column_formset = modelformset_factory(Column, form=ColumnCreationForm, extra=1)
    columns = Column.objects.none()
    formset = column_formset(request.POST or None, queryset=columns)

    context = {
        "schema_form": schema_form,
        "formset": formset
    }

    if all([schema_form.is_valid(), formset.is_valid()]):
        parent = schema_form.save()
        for form in formset:
            child = form.save()
            parent.columns.add(child)

        return HttpResponseRedirect(reverse("schema:schema-list"))
    return render(request, "schema/schema_form.html", context=context)

