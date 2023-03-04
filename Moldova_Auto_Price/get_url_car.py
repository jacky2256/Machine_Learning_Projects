from bs4 import BeautifulSoup
import requests
from get_info_car import get_info_car

def get_url_car(url):


    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'lxml')
    div_wrapper = soup.find('div', class_='wrapper')
    div_g_wrap_cf = div_wrapper.find('div', class_='g-wrap cf')
    section_container = div_g_wrap_cf.find('section', id='container')
    div_g_wrap = section_container.find('div', class_='g-wrap')
    section_items = div_g_wrap.find('section', class_='items')
    div_cf = section_items.find('div', id='js-pjax-container', class_='cf')
    div_items_row = div_cf.find('div', class_='items__row')
    div_items_list = div_items_row.find('div', class_='items__list')
    div_js_ads_container = div_items_list.find('div', id='js-ads-container', class_='items__list__container categories-map short')
    table_ads_list_table = div_js_ads_container.find('table', class_='ads-list-table')
    table_tbody = table_ads_list_table.tbody
    tbody_tr_all = table_tbody.find_all('tr')

    for tbody_tr in tbody_tr_all:

        td_ads_list_table_title = tbody_tr.find('td', class_='ads-list-table-title')
        div_ads_list_table_title_wrapper = td_ads_list_table_title.find('div', class_='ads-list-table-title-wrapper')
        h3 = div_ads_list_table_title_wrapper.h3
        span_booster_label = h3.find('span', class_='booster-label')

        if span_booster_label==None:
            
            name_auto = h3.find('a', class_='js-item-ad').text
            link_auto = h3.find('a', class_='js-item-ad').get('href')
            url_auto = "https://999.md" + link_auto
            """
            text = f"{name_auto} {url_auto}"
            with open('file.txt', 'a') as file:
                file.write(text)
                file.write('\n')
            """
            print(url_auto)
            get_info_car(url_auto)

    return True