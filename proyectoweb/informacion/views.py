from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'informacion/index.html')

def pelis(request):
    return render(request, 'informacion/pelis.html')
