from bs4 import BeautifulSoup
import requests
import os.path

def get_info_car(url):

     feature_names = {
          'name' : '',
          'group': '',
          'price': '',
          'country': '',
          'region': '',
          'url': '',
          'тип предложения': '',
          'марка' : '',
          'модель' : '',
          'регистрация' : '',
          'состояние' : '',
          'автор объявления' : '',
          'год выпуска' : '',
          'руль' : '',
          'количество мест' : '',
          'тип кузова' : '',
          'количество дверей' : '',
          'пробег' : '',
          'об. двигателя (см³)' : '',
          'мощность (л.с.)' : '',
          'тип топлива' : '',
          'кпп' : '',
          'привод' : '',
          'цвет' : '',
     }

     response = requests.get(url)
     response = response.content
     soup = BeautifulSoup(response, 'lxml')

     body = soup.body
     div_wrapper = body.find('div', class_='wrapper')
     div_g_wrap_cf = div_wrapper.find('div', class_='g-wrap cf')
     section_container = div_g_wrap_cf.find('section', id='container')
     div_g_wrap = section_container.find('div', class_='g-wrap')
     section_adPage_cf = div_g_wrap.find('section', class_='adPage cf')
     div_js_item_page = section_adPage_cf.find('div', id='js-item-page')
     div_adPage__content__inner = div_js_item_page.find('div', class_='adPage__content__inner')
     div_adPage__content__features = div_adPage__content__inner.find('div', class_='adPage__content__features')
     div_common = div_adPage__content__features.find('div', class_='adPage__content__features__col grid_9 suffix_1')
     ul_common = div_common.ul
     li_commons = ul_common.find_all('li', class_='m-value')
     
     region = get_region_price(url)

     name = get_name_seller(url)
     group, price, country, region = get_region_price(url)

     feature_names.update({'name': name})
     feature_names.update({'group': group})
     feature_names.update({'price': price})
     feature_names.update({'country': country})
     feature_names.update({'region': region})
     feature_names.update({'url': url})

     for li_common in li_commons:
          key = li_common.span
          new_value = key.find_next_sibling()
          
          key = key.text.lower().strip()
          new_value = new_value.text.lower().strip()
          feature_names.update({key:new_value})

          #old_value = feature_names.get(key)

          #try :
               #old_value.append(new_value)
               #feature_names.update(key,old_value)
          #except :
               #feature_names.update({key:new_value})

     #for key,value in features_name_2.items():
     #     print(key,value)

      #======================================================================
     # Section left - Properties
     #======================================================================
     div_adPage__content__features__col = div_adPage__content__features.find('div', class_='adPage__content__features__col grid_7 suffix_1')
     
     ul_common = div_adPage__content__features__col.ul
     #print(ul_common)
     li_commons = ul_common.find_all('li', class_='m-value')



     for li_common in li_commons:
          key = li_common.span
          new_value = key.find_next_sibling()
          
          key = key.text.lower().strip()
          new_value = new_value.text.lower().strip()
          
          feature_names.update({key:new_value})

     if os.path.exists("file.csv"):
        with open('file.csv', 'a') as file:
            for key, value in feature_names.items():
                text = f"{value},"
                file.write(text)
            file.write('\n')
     else:
          with open('file.csv', 'a') as file:
            for key, value in feature_names.items():
                text = f"{key},"
                file.write(text)
            file.write('\n')
            for key, value in feature_names.items():
                text = f"{value},"
                file.write(text)
            file.write('\n')
     
     return feature_names

def get_name_seller(url):
     name = ''
     response = requests.get(url)
     response = response.content
     soup = BeautifulSoup(response, 'lxml')

     body = soup.body
     div_wrapper = body.find('div', class_='wrapper')
     div_g_wrap_cf = div_wrapper.find('div', class_='g-wrap cf')
     section_container = div_g_wrap_cf.find('section', id='container')
     div_g_wrap = section_container.find('div', class_='g-wrap')
     section_adPage_cf = div_g_wrap.find('section', class_='adPage cf')
     #begin section with author
     aside_rightSidebar = section_adPage_cf.find('aside', class_='rightSidebar')
     div_adPage__aside__stats = aside_rightSidebar.find('div', class_='adPage__aside__stats')
     div = div_adPage__aside__stats.div
     dl_adPage__aside__stats__owner = div.find('dl', class_='adPage__aside__stats__owner')
     dd = dl_adPage__aside__stats__owner.dd
     #a_adPage__aside__stats__owner__login = dd.find('a', class_='adPage__aside__stats__owner__login buyer_experiment')
     #name = a_adPage__aside__stats__owner__login.text.strip()
     a_adPage__aside__stats__owner__login = dd.a
     name = a_adPage__aside__stats__owner__login.text

     return name

def get_region_price(url):
   
     response = requests.get(url)
     response = response.content
     soup = BeautifulSoup(response, 'lxml')

     response = requests.get(url)
     response = response.content
     soup = BeautifulSoup(response, 'lxml')

     #==============================================================
     # Pulling group of auto
     #==============================================================
     body = soup.body
     div_wrapper = body.find('div', class_='wrapper')
     div_g_wrap_cf = div_wrapper.find('div', class_='g-wrap cf')
     section_container = div_g_wrap_cf.find('section', id='container')
     div_g_wrap = section_container.find('div', class_='g-wrap')
     section_adPage_cf = div_g_wrap.find('section', class_='adPage cf')
     div_js_item_page = section_adPage_cf.find('div', id='js-item-page')
     div_adPage__content__inner = div_js_item_page.find('div', class_='adPage__content__inner')
     div_adPage__content__features = div_adPage__content__inner.find('div', class_='adPage__content__features adPage__content__features__category')

     group = div_adPage__content__features.find('div', class_='adPage__content__features__col grid_9 suffix_1').div.text

     #==============================================================
     # Pulling price of auto
     #==============================================================

     div_region_price = div_adPage__content__features.find_next('div', class_='grid_18')
     div_adPage__content__footer__wrapper = div_region_price.find('div', class_='adPage__content__footer__wrapper')
     div_js_phone_content = div_adPage__content__footer__wrapper.find('div', class_='js-phone-content adPage__content__footer__item')
     div_adPage__content__price_feature = div_js_phone_content.find('div', class_='adPage__content__price-feature')
     ul_adPage__content__price_feature__prices = div_adPage__content__price_feature.find('ul', class_='adPage__content__price-feature__prices')
     price = ul_adPage__content__price_feature__prices.li.span.text
     
     #==============================================================
     # Pulling region of auto
     #==============================================================

     dl_adPage__content__region = div_js_phone_content.find('dl', class_='adPage__content__region grid_18')

     regions = dl_adPage__content__region.find_all('dd')

     country = regions[0].text.strip()
     region = regions[1].text.strip().strip(',')

     return group, price, country, region
