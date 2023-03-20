from django.urls import path
from denek.views import DenekView


urlpatterns = [

    path('',DenekView.as_view(),name="contact"),

]