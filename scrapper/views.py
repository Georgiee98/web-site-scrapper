from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import Link

def srape(request):
    if request.method == "POST":
        site = request.POST.get('site', "")

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_adress = link.get('href')
            link_text = link.string
            Link.objects.create(adress=link_adress, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'scrapper/result.html', {'data': data})