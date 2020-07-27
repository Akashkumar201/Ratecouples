from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'name':'Fun App For Checking Couple Ratings🌟✨'})

def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    if val1[0] in ['S','K','D','P','A','V'] and val2[0] in ['M','V','L','T','S','E']:
        res='99%'
  
    elif  val1[0] in ['A','C','E'] and val2[0] in ['P','T','K']:
        res='80%'
  
    elif val1[0] in ['V','T','J','T'] and val2[0] in ['X','O','G','A']:
        res='51%'
  
    else:
        res='21%'
    return render(request,"result.html",{'result':res})
