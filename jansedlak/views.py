from django.shortcuts import render

def home(request):
    return render(request, "page.html")

def contact(request):
    return render(request, "contact.html")