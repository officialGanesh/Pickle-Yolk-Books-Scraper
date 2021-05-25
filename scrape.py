# Import the required modules

import os,csv
import requests
from requests_html import HTMLSession
from pprint import pprint

session = HTMLSession()

base_url = 'https://pickleyolkbooks.com/shop/'

user_known = ['Default','Popularity','AverageRating','Latest','LowToHigh','HighToLow']
dev_known = ['menu_order','popularity','rating','date','price','price-desc']

sort_options = dict(zip(user_known,dev_known))
# pprint(sort_options)

def Icon_slogan():
    '''Getting the logo icon and the website title'''

    r = session.get(base_url)
    r.raise_for_status
    
    try:
        logo = r.html.find('.logo',first=True)
        logo_link = logo.find('img',first=True).attrs['src']
        
        req_img = requests.get(logo_link)
        req_img.raise_for_status

        # Saving the images in local
        
        with open('Results/logo.jpg','wb') as f:
            f.write(req_img.content)
        
        
        # logo slogan in terminal
        print(f" Slogan --> {r.html.find('.logo_slogan',first=True).text}")

    except Exception as e:
        print('Something Went Wrong ',e)


if __name__ == "__main__":

    Icon_slogan()
    print('Code Completed 🔥')