from django.shortcuts import render

def accueil(request):
    return render(request, 'robotics/home.html')  # Render the homepage template