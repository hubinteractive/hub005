from django.shortcuts import render


def BaseIndex(request):
  
    
    context = {
    
    }
  
    return render(request, 'blog/index.html', context)