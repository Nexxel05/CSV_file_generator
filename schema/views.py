import csv
from pathlib import Path

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from schema.forms import SchemaCreationForm, ColumnCreationForm
from schema.models import Schema, Column, Dataset


class SchemaListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Schema
    queryset = Schema.objects.all()


class SchemaDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Schema


class SchemaDeleteView(generic.DeleteView):
    model = Schema
    success_url = reverse_lazy("schema:schema-list")


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


def create_csv(request, pk):
    data = {}
    schema = Schema.objects.get(id=pk)
    file_name = Path("{}data.csv".format(settings.MEDIA_ROOT))
    number_of_rows = int(request.GET.get("number_of_rows"))
    if number_of_rows:
        csv_dataset = Dataset.objects.create(schema=schema)
    with open(file_name, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(schema.columns.all())

        for row in range(number_of_rows):
            writer.writerow(["1", "2"])

    with file_name.open(mode="rb") as f:
        csv_dataset.dataset = File(f, name=file_name.name)
        csv_dataset.is_generated = True
        csv_dataset.save()

    if is_ajax(request=request):
        return JsonResponse(data)
    else:
        return HttpResponseBadRequest()


def download_csv(request, pk):
    dataset = Dataset.objects.get(id=pk)

    return FileResponse(dataset.dataset, as_attachment=True)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
