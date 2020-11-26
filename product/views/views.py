from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "isimler":["ismail","ahmet","mehmet"]
    }

    return render(request, template_name="product/index.html", context=context)