from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")
