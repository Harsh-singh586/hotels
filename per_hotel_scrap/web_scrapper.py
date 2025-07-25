import requests
from bs4 import BeautifulSoup
import json
import csv
import os
import random
import time

user_agents = [
    # Chrome on Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36",

    # Firefox on macOS Monterey
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.6; rv:109.0) Gecko/20100101 Firefox/115.0",

    # Edge on Windows 11
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.70 Safari/537.36 Edg/122.0.2365.80",

    # Safari on iPhone (iOS 17)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",

    # Samsung Internet on Android 13
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/110.0.5481.77 Mobile Safari/537.36",

    # Chrome on macOS Ventura
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.61 Safari/537.36",

    # Opera on Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",

    # Chrome on Android 12 (Pixel 6)
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36",

    # Safari on iPad (iPadOS 17)
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",

    # Firefox on Ubuntu Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0"
]


def get_column_values(csv_file_path, column_name):
    
    column_values = []
    try:
        with open(f"../outer_data/{csv_file_path}", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if column_name not in reader.fieldnames:
                return []  # Column not found
            for row in reader:
                column_values.append(row[column_name])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return column_values

def scrap():

    state_csv_map = [
        {
            "state" : "Delhi",
            "file" : 'data_Delhi.csv'    
        },
        {
            "state" : "Banglore",
            "file" : "data_Banglore.csv"
        },
        {
            "state" : "Manali",
            "file" : "data_Manali.csv"
        },
        {
            "state" : "Goa",
            "file" : "data_Goa.csv"
        },
        {
            "state" : "Hyderabad",
            "file" : "data_Hyderabad.csv"
        },
        {
            "state" : "Ooty",
            "file" : "data_Ooty.csv"
        },
        {
            "state" : "Darjelling",
            "file" : "data_Darjelling.csv"
        },
        {
            "state" : "Gokarna",
            "file" : "data_Gokarna.csv"
        },
        {
            "state" : "Kolkata",
            "file" : "data_Kolkata.csv"
        },
        {
            "state" : "Mumbai",
            "file" : "data_Mumbai.csv"
        },
        {
            "state" : "Munnar",
            "file" : "data_Munnar.csv"
        },
        {
            "state" : "Pondicherry",
            "file" : "data_Pondicherry.csv"
        },
        {
            "state" : "Shimla",
            "file" : "data_Shimla.csv"
        }
    ]

 
    state_data = state_csv_map[12]

    state_name = state_data['state']
    print(state_name)
    state_file = state_data['file']

    per_hotel_file_name = f'{state_name}.csv'

    url_all = get_column_values(state_file, "url")[0:1000]

    file_exists = os.path.exists(per_hotel_file_name)

    if file_exists:
        url_existing = get_column_values(per_hotel_file_name, "url")
        url_to_scrap = set(url_all) - set(url_existing)

    else:
        url_to_scrap = url_all

    print("len-------",len(url_to_scrap))

    per_hotel_data = []


    count = 0

    for url in url_to_scrap:

        count += 1

        print("count-------", count)

        num = random.randint(5, 20)
        time.sleep(num)

        headers = {
            "User-Agent": random.choice(user_agents)
        }
        request = requests.get(url, headers=headers)

        soup = BeautifulSoup(request.content, 'html.parser')


        review_score = {}

        try:
            el1 = soup.select('[data-testid="review-subscore"]')
            for i in el1:
                space_sep = i.text.split(" ")
                key = "_".join(space_sep[0 : len(space_sep)-1])
                val = space_sep[-1]
                review_score[key] = val
            review_score_string = json.dumps(review_score)
        except Exception as e:
            review_score_string = None

        checkin = ""
        checkout = ""

        try:
            house_rule = soup.select('[data-testid="HouseRules-wrapper"]')
            children_house_rule = house_rule[0].find_all('div', recursive=True)
            for i in children_house_rule:
                if "From" in i.text:
                    checkin = i.text.split(" ")[1]
                elif "Until" in i.text:
                    checkout = i.text.split(" ")[-1]
        except Exception as e:
            checkin = None
            checkout = None

        facility_list = []


        try:
            property_facility = soup.select('[data-testid="property-most-popular-facilities-wrapper"]')
            property_facility_children = property_facility[0].find_all('li', recursive=True)
            for facility in property_facility_children:
                facility_list.append(facility.text.strip())
        except Exception as e:
            pass

        facility_list_str =  json.dumps(facility_list)

        hotel_array = {
            "url" : url,
            "review_score" : review_score_string,
            "facility" : facility_list_str,
            "checkIn_time" : checkin,
            "checkOut_time" : checkout
        }

        per_hotel_data.append(hotel_array)


    try:
        with open(per_hotel_file_name, 'a', newline='\n') as csvfile:
            fieldname = ["url", "review_score", "facility", "checkIn_time", "checkOut_time"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldname)
            if not file_exists:
                writer.writeheader()
            writer.writerows(per_hotel_data)
    except Exception as e:
        print("error in writing file", e)
        if os.path.exists(per_hotel_file_name):
            os.remove(per_hotel_file_name)


scrap()