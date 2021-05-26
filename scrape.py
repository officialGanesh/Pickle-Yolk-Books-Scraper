# Import the required modules

import csv
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

def Various_books_info():
    '''Getting the varoius books info'''


    for options in sort_options:
        
        url = f"{base_url}?orderby={sort_options[options]}"
        # print(url)
        r = session.get(url)
        r.raise_for_status

        posts = r.html.find('.post_item_wrap')
        
        csv_file = open(f'Results/{sort_options[options]}.csv','w',newline='')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title','Price','Image'])

        for post in posts:
            
            try:
                title = post.find('h2',first=True).text
                # print(title)
                    

                price = post.find('bdi',first=True).text
                # print(price)
                    

                img_link = post.find('img',first=True).attrs['src']
                # print(img_link)

                    
            except Exception as e:
                print('Something Went Wrong ',e)

            csv_writer.writerow([title,price,img_link])
        csv_file.close()    

if __name__ == "__main__":

    # Icon_slogan()
    Various_books_info()

    print('Code Completed 🔥')