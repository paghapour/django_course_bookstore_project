from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    TemplateView = 'home.html'
