from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306206282',
        'name': 'Fathurrahman Kesuma Ridwan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)