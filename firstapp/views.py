from django.shortcuts import render

# Create your views here.

# this is for loading first_page(first.html)
def firstpage(request):
    return render(request,'first.html')

def secondpage(request):
    return render(request,'second.html')