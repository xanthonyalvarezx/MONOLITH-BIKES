from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    return render(request, 'contact.html', {})
