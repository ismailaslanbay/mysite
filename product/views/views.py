from django.shortcuts import render

# Create your views here.
from ..models import *

def index(request):

    products = Product.objects.all()
    context = {
        "products" : products
    }

    return render(request, template_name="product/index.html", context=context)