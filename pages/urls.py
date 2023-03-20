from django.urls import path
from pages.views import ContactView


urlpatterns = [

    path('',ContactView.as_view(),name="contact1"),

]