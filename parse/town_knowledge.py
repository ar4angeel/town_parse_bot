import requests
from bs4 import *


html_wiki_towns = requests.get('https://ru.wikipedia.org/wiki/Городские_населённые_пункты_Московской_области')
r_html_towns = html_wiki_towns.text
hot_soup = BeautifulSoup(r_html_towns, 'html.parser')
warmed_over_soup = hot_soup.find('div', class_='mw-body-content mw-content-ltr')
warm_soup = warmed_over_soup.find('table')

room_temp_soup = warm_soup.find('tbody')

a = room_temp_soup.find_all('td',style='text-align:center')
b = a[0:223:3]

def search_name_by_tr(number):
    a = b[number].find_previous(('tr'))
    c = a.find_all('a')
    print(c)

numbere = input()
search_name_by_tr(int(numbere))

class Structure:
    def init(self):
