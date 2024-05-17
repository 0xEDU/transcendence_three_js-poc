from django.shortcuts import render

# Create your views here.


def three_js_view(request):
    print("oi")
    return render(request, 'index.html')
