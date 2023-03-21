import time
import requests
import json
import googlemaps
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#Entrada da chave API
API_KEY = 'AIzaSyCl7yPcnmda506d_zUDj89bgFEij0fdfUU'
map_client = googlemaps.Client(API_KEY)

#Leitura do arquivo de entrada
address=pd.read_excel('address.xlsx')

def find_info(df, field):
    info_list = []
    for i in range(len(df.index)):
        placeIDpayload = {'key': API_KEY, 'place_id': str(df.iat[i,1]), 'fields': field}
        query = requests.get('https://maps.googleapis.com/maps/api/place/details/json?', params=placeIDpayload)
        result = query.json()['result']
        info_list.append(result.get(field))
    df[field] = info_list       

      
df = pd.DataFrame()
for i in range(len(address.index)):
    
    print((i/len(address.index)*100),'%', " - ", address.iat[i,0],)

    try:
        geocode = map_client.geocode(address=address.iat[i,0])
        (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

        search_string = 'construtora'
        distance = 2000000
        business_list = []

        response = map_client.places_nearby(
            location=(lat, lng),
            keyword=search_string,
            radius=distance
        )   

        business_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

        while next_page_token:
            time.sleep(2)
            response = map_client.places_nearby(
                location=(lat, lng),
                keyword=search_string,
                radius=distance,
                page_token=next_page_token
            )   
            business_list.extend(response.get('results'))
            next_page_token = response.get('next_page_token')
        
            df = pd.concat([df, pd.DataFrame(business_list)])
            df = df.drop(columns=['business_status', 'geometry', 'icon', 'icon_background_color','icon_mask_base_uri', 'opening_hours', 'photos', 'plus_code','reference', 'scope','types','user_ratings_total', 'vicinity'])
            find_info(df, "formatted_address")
            find_info(df,"website")
    except:
        pass


df = df[['name','website','formatted_address','rating']]
df.sort_values('rating', axis=0, ascending=False, inplace=True, na_position='last')
df = df.drop(columns=['rating'])  

df.to_excel('{0}.xlsx'.format(search_string), index=False)