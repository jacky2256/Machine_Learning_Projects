from get_url_car import get_url_car
from get_info_car import get_info_car


for i in range(1,3):
    url = f'https://999.md/ru/list/transport/cars?view_type=short&page={i}'
    if get_url_car(url) :
        print(f'Str={i} {url} True')
    else:
        print(f'Str={i} {url} False')

#url = 'https://999.md/ru/80782423'
#get_info_car(url)

