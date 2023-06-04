from django.urls import reverse_lazy
from django.views import generic

from cable_app_0_1.cable.forms import CableCreateForm, MachineCreateForm, CapCreateForm, ClutchCreateForm, \
    InductorCreateForm
from cable_app_0_1.cable.models import Cable, Machine, Cap, Clutch, Inductor


class IndexView(generic.ListView):
    model = Cable
    template_name = 'cables/index.html'
    paginate_by = 10
    queryset = Cable.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["cables"] = Cable.objects.all()
    #     return context


class CableCreateView(generic.CreateView):
    model = Cable
    template_name = 'cables/cable_create.html'
    form_class = CableCreateForm
    success_url = reverse_lazy('home page')


class CableDetailsView(generic.DetailView):
    template_name = 'cables/cable_details.html'
    model = Cable


class CableEditView(generic.UpdateView):
    model = Cable
    template_name = 'cables/cable_edit.html'
    form_class = CableCreateForm

    def get_success_url(self):
        return reverse_lazy('cable details', kwargs={
            'pk': self.object.pk
        })


class CableDeleteView(generic.DeleteView):
    model = Cable
    template_name = 'cables/cable_delete.html'
    success_url = reverse_lazy('home page')


class MachineCreateView(generic.CreateView):
    model = Machine
    template_name = 'cables/component_create.html'
    form_class = MachineCreateForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = 'Machine'
        return context


class MachineDetailsView(generic.DetailView):
    model = Machine
    template_name = 'cables/component_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = self.object.name
        return context


class CapCreateView(generic.CreateView):
    model = Cap
    template_name = 'cables/component_create.html'
    form_class = CapCreateForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = 'Cap'
        return context


class CapDetailsView(generic.DetailView):
    model = Cap
    template_name = 'cables/component_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = self.object.name
        return context


class ClutchCreateView(generic.CreateView):
    model = Clutch
    template_name = 'cables/component_create.html'
    form_class = ClutchCreateForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = 'Clutch'
        return context


class ClutchDetailsView(generic.DetailView):
    model = Clutch
    template_name = 'cables/component_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = self.object.name
        return context


class InductorCreateView(generic.CreateView):
    model = Inductor
    template_name = 'cables/component_create.html'
    form_class = InductorCreateForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = 'Inductor'
        return context


class InductorDetailsView(generic.DetailView):
    model = Inductor
    template_name = 'cables/component_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component"] = self.object.name
        return context
