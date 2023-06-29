from django.shortcuts import render, HttpResponse
from .models import Company

# Create your views here.
def home(request):
    result = Company.objects.all()
    return render(request, 'companies.html', {'companies': result})

def get_company(request, pk):
    result = Company.objects.filter(pk=pk).first()
    return render(request, 'company.html', {'company': result})
