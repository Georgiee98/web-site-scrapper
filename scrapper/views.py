from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Link

def srape(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    for link in soup.find_all('a'):
        link_adress = link.get('href')
        link_text = link.string
        Link.objects.create(adress=link_adress, name=link_text)

    data = Link.objects.all()
    return render(request, 'scrapper/result.html', {'data': data})