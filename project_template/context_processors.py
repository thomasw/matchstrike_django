from django.conf import settings

def default(request):
	"""Adds 'DEBUG, SITE_NAME, path, and domain to the default context."""
	return {'DEBUG': getattr(settings,'DEBUG', False), 
			'SITE_NAME': getattr(settings,'SITE_NAME', False),
			'path': request.META['PATH_INFO'],
			'domain':request.get_host(),}