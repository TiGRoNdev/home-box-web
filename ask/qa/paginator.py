from django.core.paginator import Paginator
from django.http import Http404

def paginate(request, qs, baseurl):
	try:
		limit = int(request.GET.get('limit', 10)
	except ValueError:
		limit = 10
	try:
		page = int(request.GET.get('page', 1)
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	paginator.baseurl = baseurl
	page = paginator.page(page)
	return paginator, page
