from django.shortcuts import render
#from django.http import HttpResponse

#def index(requests):
   # return HttpResponse('Успешно!')

def index(request):
    return render(request, 'index.html')



def top_sellers(request):
    return render(request, 'top-sellers.html')



def register(request):
    return render(request, 'register.html')

# Create your views here.
