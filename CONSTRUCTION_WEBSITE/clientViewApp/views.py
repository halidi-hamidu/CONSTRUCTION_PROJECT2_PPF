from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def homePage(request):
  template_name ='homePage.html'
  context = {

  }
  return render(request, template_name, context)

def aboutPage(request):
  template_name ='aboutPage.html'
  context = {

  }
  return render(request, template_name, context)


def contactPage(request):
  template_name ='contactPage.html'
  context = {

  }
  return render(request, template_name, context)

def servicePage(request):
  template_name ='servicePage.html'
  context = {

  }
  return render(request, template_name, context)

def portfolioPage(request):
  template_name ='portfolioPage.html'
  context = {

  }
  return render(request, template_name, context)