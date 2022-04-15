from django.shortcuts import render

# Create your views here.
def qualif(request):
    context={'qualif':'active'}
    return render(request,'qual/edu.html',context)
