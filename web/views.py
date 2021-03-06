import os
import json

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('index.html')

	"""
	This placeholder data will be loaded from .json files,
	and eventually generated dynamically.
	"""

	context = RequestContext(request, {
		'name' : 'Learn the Greek Alphabet',
		'content' : '...'
	})

	return HttpResponse(template.render(context))
