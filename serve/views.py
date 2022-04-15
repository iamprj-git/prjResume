from django.shortcuts import render
def service(request):
    context={'services':'active'}
    return render(request,'serv/services.html')

# Create your views here.
