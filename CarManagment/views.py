from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


from .models import Car, Service, ServiceHistory


class IndexView(ListView):
    model = Car
    template_name = 'CarManagement/pages/index.html'
    context_object_name = 'cars'


class CarCreateView(CreateView):
    model = Car
    template_name = 'CarManagement/pages/car_create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'CarManagement/pages/car_edit.html'
    fields = ('mileage',)
    success_url = reverse_lazy('index')
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
          ctx = super().get_context_data(**kwargs)
          ctx['services'] = Service.objects.all()
          return ctx


class HistoryCreateView(CreateView):
    model = ServiceHistory
    template_name = 'CarManagement/pages/history_create.html'
    fields = ('service', 'car',)
    success_url = reverse_lazy('index')
