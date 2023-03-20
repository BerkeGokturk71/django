from django.views.generic.edit import FormView
from .forms import DenekForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class DenekView(FormView,SuccessMessageMixin):
    template_name = "contact1.html"
    form_class = DenekForm
    success_url = reverse_lazy('contact')
    success_message = "We received your mail"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)