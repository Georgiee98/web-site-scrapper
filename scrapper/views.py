from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def srape(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    link_adress = []
    for link in soup.find_all('a'):
        link_adress.append(link.get('href'))
    return render(request, '/scrapper/index.html', {'page': link_adress})



