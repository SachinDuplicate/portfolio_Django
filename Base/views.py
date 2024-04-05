from django.shortcuts import render ,redirect
from Base.models import Contact 
def home(request):
    return render(request,'home.html')

def contact(request):
   
   return render(request,'home.html') 


  
