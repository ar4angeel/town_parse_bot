import requests
from bs4 import *
from some_models import Towns

html_wiki_towns = requests.get('https://ru.wikipedia.org/wiki/Городские_населённые_пункты_Московской_области')
r_html_towns = html_wiki_towns.text
hot_soup = BeautifulSoup(r_html_towns, 'html.parser')
warmed_over_soup = hot_soup.find('div', class_='mw-body-content mw-content-ltr')
warm_soup = warmed_over_soup.find('table')

room_temp_soup = warm_soup.find('tbody')

a = room_temp_soup.find_all('td',style='text-align:center')
position_of_slice_in_list = a[0:223:3]


def search_by_tr(number, name):
    info_in_slice_of_table = position_of_slice_in_list[number].find_previous(('tr'))
    find_name = info_in_slice_of_table.find_all('td')
    a = find_name[name]
    return a


def new_record():
    for data in range(0,74):
        count = data
        town = search_by_tr(data,1).text
        district = search_by_tr(data,2).text
        okato = search_by_tr(data,3).text
        population = search_by_tr(data, 4).text
        year_foundation = search_by_tr(data, 5).text
        assignment_sity = search_by_tr(data, 6).text
        Towns.create(count=count, town=town, district=district, okato=okato, population=population,year_foundation=year_foundation,assignment_sity=assignment_sity)

new_record()
