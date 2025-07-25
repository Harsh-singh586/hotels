from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random
import json
import csv

def scrap(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome('/opt/chromedriver/chromedriver',chrome_options=options)

    checkIn = "2025-07-01"
    checkOut = "2025-07-07"

    url_map = [{
        "url": f"https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi&ssne=New+Delhi&ssne_untouched=New+Delhi&efdco=1&label=in-new-delhi-e8W1ee8F8u0VtKbPZDZV*wS553191848784%3Apl%3Ata%3Ap11020%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-186693036%3Alp9215535%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2106102&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Delhi"
    },
    {
        "url": f'https://www.booking.com/searchresults.en-gb.html?ss=Hyderabad&ssne=Hyderabad&ssne_untouched=Hyderabad&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Aq6bz8EGwAIB0gIkMmI4ZjY1ZjYtZTk4Yi00ODgzLWI3MzctNTlmMDY0ZmI2OWU22AIF4AIB&sid=6a79f3b0e2eed797e56fbbbc032eb85b&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2097701&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0',
        "city" : "Hyderabad"

    },
    {
        "url" : f'https://www.booking.com/searchresults.en-gb.html?ss=Mumbai&ssne=Mumbai&ssne_untouched=Mumbai&efdco=1&label=bombay-ojXiksgy7PQEP4LUUIOBsgS525624659405%3Apl%3Ata%3Ap1480%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-25100521%3Alp1007765%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2092174&dest_type=city&checkin={checkIn}&checkout={checkOut}c&group_adults=2&no_rooms=1&group_children=1&&age=0',
        "city" :"Mumbai"
    },
    {
        "url" : f'https://www.booking.com/searchresults.en-gb.html?ss=Kolkata&ssne=Kolkata&ssne_untouched=Kolkata&efdco=1&label=in-calcutta-vvLzfPkAAQzI7P35JNnmXgS528846144629%3Apl%3Ata%3Ap1270%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-139994056%3Alp1007765%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2092511&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0',
        "city" : "Kolkata"
    },
    {
        "url" : f'https://www.booking.com/searchresults.en-gb.html?ss=Bengaluru&ssne=Bengaluru&ssne_untouched=Bengaluru&efdco=1&label=in-bangalore-IvEBMI8evXKgb5K6o*nE5gS525624658703%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-25100511%3Alp1007765%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&sid=be08456c30f4f65c80ad3e6d40b384ca&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2090174&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0',
        "city" : "Banglore"
    },
    {
        "url" : f'https://www.booking.com/searchresults.en-gb.html?ss=Man%C4%81li&ssne=Man%C4%81li&ssne_untouched=Man%C4%81li&efdco=1&label=manali-*dOCXSLs7S8rLe_i*dquYwS392972668748%3Apl%3Ata%3Ap1200%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-25100481%3Alp1007765%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2103603&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0',
        "city" : "Manali"
    },
    {
        "url" : f'https://www.booking.com/searchresults.en-gb.html?ss=Shimla&ssne=Shimla&ssne_untouched=Shimla&efdco=1&label=simla-OrcOJ63hB4vu2WWSYE6MrQS650545857084%3Apl%3Ata%3Ap195%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-1698310051%3Alp1007765%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2111367&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0',
        "city" : "Shimla"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Darjeeling&ssne=Darjeeling&ssne_untouched=Darjeeling&efdco=1&label=in-darjeeling-Ap7suPadgvusSejW_mkkPQS528846144620%3Apl%3Ata%3Ap180%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-749318718%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2094056&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Darjelling"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Ooty&ssne=Ooty&ssne_untouched=Ooty&efdco=1&label=udagamandalam-QNvSsbKFBcfcVFU*asFKOgS392972668511%3Apl%3Ata%3Ap1115%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-184918236%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2113628&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Ooty"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Munnar&ssne=Munnar&ssne_untouched=Munnar&efdco=1&label=munnar-fEyoWE*r4vqPyXcmF1STAAS392710364838%3Apl%3Ata%3Ap1180%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-548904691%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2105113&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Munnar"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Goa&ssne=Goa&ssne_untouched=Goa&efdco=1&label=goa-ZeZjr8EI44AA*FPJ9u*FqgS388387535727%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-25100501%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcWHiCDB7igB8XpJKYgu4TM&aid=324798&lang=en-gb&sb=1&src_elem=sb&src=region&dest_id=4127&dest_type=region&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Goa"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Puducherry&ssne=Puducherry&ssne_untouched=Puducherry&efdco=1&label=pondicherry-5YiIKp6IDdMxZqtRDo96agS553184227320%3Apl%3Ata%3Ap190%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-1918084288%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2108165&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Pondicherry"
    },
    {
        "url" : f"https://www.booking.com/searchresults.en-gb.html?ss=Gokarna&ssne=Gokarna&ssne_untouched=Gokarna&efdco=1&label=gokarna-in-VKOvbFwRZ45xs24a_OdV2QS392822631354%3Apl%3Ata%3Ap110%3Ap2300%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-6666149201%3Alp9181766%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&aid=306395&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=900051864&dest_type=city&checkin={checkIn}&checkout={checkOut}&group_adults=2&no_rooms=1&group_children=1&age=0",
        "city" : "Gokarna"
    }
    ]



    link = url_map[12]
    #import pdb; pdb.set_trace();
    driver.get(link.get('url'))

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


    error_file = open(f"error_{link.get('city')}.txt", "w")
    for hotel in el:
        try:
            url = hotel.select_one('[data-testid="title-link"]')['href']
        except Exception as e:
            url = ""
            error_str = f'hotel name --- {name}, key -- url, error -- {str(e)} \n'
            error_file.write(error_str)
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
                review_count_txt = review_description[1].text
                if "," in review_count_txt:
                    review_count_txt = review_count_txt.replace(",", "")
                if "reviews" in review_count_txt:
                    review_count = int(review_count_txt.replace(" reviews", ""))
                elif "review" in review_count_txt:
                    review_count = int(review_count_txt.replace(" review", ""))
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
                    "checkin": checkIn,
                    "checkout" : checkOut,
                    "city" : link.get('city'),
                    "url" : url}
        hotel_array.append(hotel_data)

    driver.quit()

    print("final hotel array", len(hotel_array))

    with open(f"data1_{link.get('city')}.csv", "w", newline='', encoding='utf-8') as file:
        fieldnames = hotel_array[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() 
        writer.writerows(hotel_array)
    error_file.close()



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


'''
>>> propert_high = soup.find_all('div', class_ = "property-highlights ph-icon-fill-color")
>>> li_items1 = propert_high[0].find_all('p', recursive=True)
>>> highlight_array = []
>>> for higlight in li_items1:
...    highlight_array.append(higlight.text.strip())
... 
>>> highlight_array
['Vegetarian, Vegan', 'City view', 'Free private parking available at the hotel', '']
>>> 

-------------------------------------------------------------------------------------
>>> property_facility = soup.select('[data-testid="property-most-popular-facilities-wrapper"]')
>>> li_items = property_facility[0].find_all('li', recursive=True)
>>> 
>>> li_items[0].text
'Free parking 

>>> li_items = property_facility[0].find_all('li', recursive=True)
>>> 
>>> facility_list = []
>>> 
>>> for facility in li_items:
...    facility_list.append(facility.text.strip())
... 
>>> 
>>> facility_list
['Free parking', 'Free WiFi', 'Room service', 'Facilities for disabled guests', 'Family rooms', '24-hour front desk', 'Terrace', 'Tea/coffee maker in all rooms', 'Breakfast', 'Free cot available on request']

-------------------------------------------------------------------------------------------------------


el = soup.select('[data-testid="review-score-right-component"]')
>>> review_div = el[0].find_all('div', recursive=True)

 for x in review_div:
...    if 'review' in x.text:
...      r = x.text
...    try:
...      score = float(x.text)
...      score_found = 1
...    except:
...      if not score_found:
...          score = None

----------------------------------------------------------------------------

>>> el1 = soup.select('[data-testid="review-subscore"]')

>>> for i in el1:
...    if "Value for money" in i.text:
...       value = i.text.split(" ")[-1]
...       key = "Value_for_money"
...    else:
...       key, val = i.text.split(" ")
...    a[key] = val

------------------------------------------------------------------------

>>> loc = soup.find_all('span', class_ = 'review-score-widget')
loc[0].text.strip()


'''
