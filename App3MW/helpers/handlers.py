from django.shortcuts import render


def handler404(request):
    return render(request, 'handlers/404.html', {
        'title': '400 - Not found'
    })


def handler500(request):
    return render(request, 'handlers/500.html', {
        'title': '500 - Internal Server error'
    })
