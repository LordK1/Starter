from django.views.generic.base import TemplateView

__author__ = 'k1'


class HomeView(TemplateView):
    """
    this view hande Home page
    """
    template_name = "home.html"


class AboutView(TemplateView):
    """
    About us page
    """
    template_name = "abount.html"
