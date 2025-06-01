from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from database import insert_data
import random
import json

options = Options()
#options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

driver.get('https://www.booking.com/searchresults.en-gb.html?ss=Hyderabad&ssne=Hyderabad&ssne_untouched=Hyderabad&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Aq6bz8EGwAIB0gIkMmI4ZjY1ZjYtZTk4Yi00ODgzLWI3MzctNTlmMDY0ZmI2OWU22AIF4AIB&sid=6a79f3b0e2eed797e56fbbbc032eb85b&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2097701&dest_type=city&checkin=2025-06-01&checkout=2025-06-07&group_adults=2&no_rooms=1&group_children=1&age=0')

last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
hotel_array = []
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    num = random.randint(30, 60)
    time.sleep(num)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    button = driver.find_elements(By.TAG_NAME, 'button')
    load_button = [b for b in button if b.text == "Load more results"]
    if load_button:
        load_button[0].click()
    count += 1
    print("count -----------", count)
  
    


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
el = soup.select('[data-testid="property-card-container"]')


error_file = open("error.txt", "w")
for hotel in el:
    try:
        name = hotel.select_one('[data-testid="title"]').text
    except Exception as e:
        name = ""
        error_str = f'hotel name --- {name}, key -- name, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        room_type = hotel.find('h4').text
    except Exception as e:
        room_type = ""
        error_str = f'hotel name --- {name}, key -- room_type, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        strong = hotel.find_all('strong')
        try:
            cancelType = strong[0].text
        except Exception as e:
            cancelType = ""
            error_str = f'hotel name --- {name}, key -- cancelType, error -- {str(e)} \n'
            error_file.write(error_str)
        try:
            paymentType = strong[1].text
        except Exception as e:
            paymentType = ""
            error_str = f'hotel name --- {name}, key -- paymenttype, error -- {str(e)} \n'
            error_file.write(error_str)
    except Exception as e:
        cancelType = ""
        paymentType = ""
        error_str = f'hotel name --- {name}, key -- paymentType CancelType, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        bedType = hotel.find('li').text
    except Exception as e:
        bedType = ""
        error_str = f'hotel name --- {name}, key -- bedType, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        price = hotel.select_one('[data-testid="price-and-discounted-price"]').text
    except Exception as e:
        price = ""
        error_str = f'hotel name --- {name}, key -- price, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        review_div = hotel.select_one('[data-testid="review-score"]')
        review_child = review_div.find_all('div', recursive=False)
        try:
            review = review_child[1].text
        except Exception as e:
            review = -1
            error_str = f'hotel name --- {name}, key -- review, error -- {str(e)} \n'
            error_file.write(error_str)
        try:
            review_description = review_child[2].find_all('div', recursive=False)
            review_count = int(review_description[1].text.replace(" reviews", ""))
        except Exception as e:
            review_count = -1
            error_str = f'hotel name --- {name}, key -- review count, error -- {str(e)} \n'
            error_file.write(error_str)
    except Exception as e:
        review_count = -1
        review = -1
        error_str = f'hotel name --- {name}, key -- review review_count, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        distance = hotel.select_one('[data-testid="distance"]').text
    except Exception as e:
        distance = ""
        error_str = f'hotel name --- {name}, key -- distance, error -- {str(e)} \n'
        error_file.write(error_str)
    try:
        address= hotel.select_one('[data-testid="address"]').text
    except Exception as e:
        address = ""
        error_str = f'hotel name --- {name}, key -- address, error -- {str(e)} \n'
        error_file.write(error_str)
    checkout="2025-06-15"
    checkin="2025-06-14"

    hotel_data = {"name" : name,
                  "room_type" : room_type,
                  "cancel_type" : cancelType,
                  "paymentType" : paymentType,
                  "bed_type" : bedType,
                  "price" : price,
                  "review" : review,
                  "review_count" : review_count,
                  "distance" : distance,
                  "address": address,
                  "checkin": checkin,
                  "checkout" : checkout}
    hotel_array.append(hotel_data)
        

driver.quit()

print(len(hotel_array))
with open("data.json", "w") as file:
    file.write(json.dumps(hotel_array))
error_file.close()
insert_data(hotel_array)


'''
el = soup.select('[data-testid="property-card-container"]')
(Pdb) name = el[0].select_one('[data-testid="title"]').text
(Pdb) room_type = el[0].find('h4').text
(Pdb) strong = el[0].find_all('strong')
(Pdb) strong[0].text
'Free cancellation'
(Pdb) strong[1].text
'No prepayment needed'
(Pdb) el[0].find('li').text
'1 large double bed'
(Pdb) bed_type = el[0].find('li').text
(Pdb) discount_price = el[0].select_one('[data-testid="price-and-discounted-price"]').text
(Pdb) review_div = el[1].select_one('[data-testid="review-score"]')
(Pdb) review = review_div.find_all('div', recursive=False)
(Pdb) len(review)
3
(Pdb) review[0].text
'Scored 7.7 '
(Pdb) review[1].text
'7.7'
(Pdb) review[2].text
'Good 961 reviews'
(Pdb) review_description = review2.find_all('div', recursive=False)
*** NameError: name 'review2' is not defined
(Pdb) review_description = review[2].find_all('div', recursive=False)
(Pdb) review_description[1].text
'961 reviews'
(Pdb) name
'Hotel O 11 Eleven'
(Pdb) el[1].find('li').text
'Private suite • 1 bedroom • 1 living room • 1 bathroom • 46m²2 beds (1 sofa bed, 1 large double)'
(Pdb) el[1].select_one('[data-testid="distance""]')
*** soupsieve.util.SelectorSyntaxError: Malformed attribute selector at position 0
  line 1:
[data-testid="distance""]
^
(Pdb) el[1].select_one('[data-testid="distance"]')
<span data-testid="distance" role="button" tabindex="0">9.7 km from centre</span>
(Pdb) el[1].select_one('[data-testid="distance"]').text
'9.7 km from centre'
(Pdb) distance = el[1].select_one('[data-testid="distance"]').text
(Pdb) el[1].select_one('[data-testid="address"]').text
'Gachibowli, Hyderabad (Gachibowli)'
(Pdb) address = el[1].select_one('[data-testid="address"]').text




(Pdb) names[0]
'Oakwood Residence Kapil Hyderabad'
(Pdb) address[0]
'Hyderabad'
(Pdb) distance[0]
'10.6 km from centre'
(Pdb) discount[0]
'₹\xa06,000'
(Pdb) bed_types[0]
'1 large double bed'
(Pdb) len(strong[0])
1
(Pdb) len(strong[1])
2
(Pdb) len(strong[2])
2
(Pdb) len(strong[3])
1
(Pdb) max([len(a) for a in strong])
2
(Pdb) strong[0].text
*** AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
(Pdb) strong[0][0].text
'Free cancellation'
(Pdb) strong[1][1].text
'No prepayment needed'
(Pdb) strong[1][0].text
'Free cancellation'
(Pdb) room_types[0]
'Studio Superior '
(Pdb) names[0]
'Oakwood Residence Kapil Hyderabad'
'''