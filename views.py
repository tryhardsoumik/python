from django.shortcuts import render

# Create your views here.
def index(request):
    context={

"welcome-text":"this is index page",

    }
    return render(request,'index.html',context)

def contact(request):
    context={
"welcome-text":"this is contact page",


    }
    return render(request,'contact.html',context)
        
def Aboutus(request):
    context={

"welcome-text":"this is AboutUs page",

    }
    return render(request,'Aboutus.html',context)
    
    