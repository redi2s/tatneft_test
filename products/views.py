from django.shortcuts import render_to_response
from django.template import RequestContext
from products.models import Nomenclature


def show_genres(request):
    nomenclature = Nomenclature.objects.all()
    return render_to_response('index.html', {'nodes': nomenclature})

# return render_to_response("genres.html", {'nodes': nodes, 'current_category': current_category, 'root_category_id': root_category_id}, context_instance=RequestContext(request))