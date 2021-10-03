from django.shortcuts import render
from .models import About


def about_us(request):
    all_about = About.objects.all()
    return render(request, 'about/about_us.html', context={
        'all_about': all_about
    })
