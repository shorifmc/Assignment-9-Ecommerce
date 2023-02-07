from django.shortcuts import render

# Create your views here.
def getLaptop(request):
    return render(request, 'laptop.html')