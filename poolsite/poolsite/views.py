from django.shortcuts import render , get_object_or_404 , redirect


def home_page(request):
    template_name = "home.html"    
    return render(request, template_name)

    