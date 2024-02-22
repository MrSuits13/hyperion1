from django.shortcuts import render

# Create your views here.
def about_me(request):
    return render(request, 'about_me.html')

def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    return render(request, 'contact.html')