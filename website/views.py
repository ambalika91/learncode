from django.shortcuts import render
from django.views.generic import FormView, RedirectView, TemplateView

#View for index page
class index(TemplateView):

    #sent the template name
    template_name = 'index.html'


