from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,'front.html')


def next_page(request):
    return render(request,'blackchat/home.html')