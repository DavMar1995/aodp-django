from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# class 

def japanDashboard(request):
    return render(request, 'visitor/japan/各大洲訪日外客數儀表板.html', {})

def numberOfForeignToJapan(request):
    return render(request, 'visitor/japan/Number_of_foreign_visitors_to_Japan.html')