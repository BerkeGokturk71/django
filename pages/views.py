from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class ContactView(FormView,SuccessMessageMixin):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "We received your mail"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)