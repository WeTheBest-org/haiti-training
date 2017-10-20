# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView
from django.core.serializers import serialize

from .models import MapImage
from .forms import MapImageForm

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'all_map_image'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['geojson'] = serialize('geojson', MapImage.objects.all(), geometry_field='location', fields=('name', 'pk', 'image'))
		return context

	def get_queryset(self):
		return MapImage.objects.all()

class InsertView(FormView):
	template_name = 'map_image_form.html'
	form_class = MapImageForm
	success_url = '/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed
		post = form.save(commit=False)
		post.name = self.request.POST.get('name')
		post.image = self.request.FILES.get('image')
		post.location = self.request.POST.get('location')
		post.save()
		return super(InsertView, self).form_valid(form)

class MapDetailView(DetailView):
	template_name = 'map_detail.html'
	model = MapImage

class MapUpdateView(UpdateView):
	"""docstring for MapUpdateView"""
	model = MapImage
	form_class = MapImageForm
	template_name = 'map_image_update.html'
	success_url = '/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed
		post = form.save(commit=False)
		image = self.request.FILES.get('image')
		if image:
			post.image = image
		post.name = self.request.POST.get('name')
		post.location = self.request.POST.get('location')
		post.save()
		return super(MapUpdateView, self).form_valid(form)
