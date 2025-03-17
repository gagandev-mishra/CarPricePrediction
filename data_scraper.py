import requests
import json
import pandas as pd
import time

# CarDekho API URL
base_url = "https://listing.cardekho.com/api/v1/srp-listings"

# To hold the unique of vehcile listing
vehicle_central_id = []
# Store overall car data from the https://www.cardekho.com/used-cars
car_data = []
# Store the detail information about car
car_spec = {}

# Pagination pattern
page_step = 20  # Change this based on observed behavior
pagination_step = 15
total_pages = 500  # Adjust as needed

urls = []  # Store generated URLs

# Set the header to avoid blocking
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0', 'Referer': 'https://www.google.com/'}

# Set the number of page to extract and put the parameters to pass while extracting
# Generate URLs dynamically
for i in range(total_pages):
    pagefrom = i * page_step
    pagination = json.dumps({
        "common": (i + 1) * pagination_step,
        "commonFeature": (i + 1) * 5,  # Adjust based on observed behavior
        "carAd": 0
    })

    params = {
    "cityId": "",
    "connectoid": "",
    "sessionid": "a6bde3c9ca870ed1c46b18a5a2d06f5f",
    "lang_code": "en",
    "regionId": "0",
    "searchstring": "used-cars",
    "sortby": "",
    "sortorder": "desc",
    "mink": "",
    "maxk": "",
    "dealer_id": "null",
    "regCityNames": "",
    "regStateNames": "",
    "cellValue": "",
    "device": "web",
    "userLat": "",
    "userLng": "",
    "platform": "web",
    "pagefrom": pagefrom,
    "pagination": pagination  # JSON formatted pagination
}

    response = requests.get(base_url, params=params, headers=headers)
    
    # If the status is 200, then execute the following lines of code, and store data in json 
    if response.status_code == 200:
        data = response.json()

    # Store the necessary infomration that I want to keep    
    for car in data['data']['cars']:
        car_data.append({
                        'usedCarId': car['usedCarId'],'centralVariantId': car['centralVariantId'], 'model_year': car['myear'], 'model_name': car['model'],
                        'variant_name': car['variantName'], 'car_oem': car['oem'],'car_type': car['bt'],'owner': car['owner'], 'owner_slug': car['ownerSlug'],
                        'km': car['km'], 'ft': car['ft'], 'tt': car['tt'], 'msp': car['msp'], 'city': car['city']
                        })
        # Also making note of centralVariantId to find more details about car
        vehicle_central_id.append(car['centralVariantId'])
    
    time.sleep(1.5)

# Required Features
required_features = [
    "Engine Type", "Displacement", "Max Power", "Max Torque", "No. of Cylinders", "Valves Per Cylinder", "Emission Norm Compliance","Drive Type", "Gearbox", "Steering Type",
    "Drive Type", "Mileage", "Length", "Width", "Height", "Ground Clearance Unladen", "Kerb Weight","Seating Capacity", "Wheel Base", "No. of Doors"
]

#  Above just extracted handful of information about car, and seller, but the following line of code will extract the car technical information
row_extracted = 0
for vlink_id in vehicle_central_id:
    # https://www.cardekho.com/api/v1/usedcar/specs?&cityId=&connectoid=&sessionid=dc58effe83d533529880f6db5f2ca75a&lang_code=en&regionId=0&otherinfo=all&variantId=1549
    specs_url = f"https://www.cardekho.com/api/v1/usedcar/specs?variantId={vlink_id}&otherinfo=all"
    specs_response = requests.get(specs_url, headers=headers)
    
    # Check for the response status, and move forward to store 
    if specs_response.status_code == 200:
        specs_data = specs_response.json()
        
        for features in specs_data['data']['carSpecification']['data']:
            for inner_feature in features['list']:
                key = inner_feature['key']
                value = inner_feature['value']
                
                # Store only required features
                if key in required_features:
                    if vlink_id not in car_spec:
                        car_spec[vlink_id] = {}  # Store as dictionary

                    car_spec[vlink_id][key] = value  # Save as key-value pair

        row_extracted += 1
        print(f"No. of row {row_extracted} extracted sucessfully!")
        time.sleep(1.5)

    else:
        print(f"Failed to fetch specs for {vlink_id}")


# Convert dictionary to Pandas DataFrame
car_data_df = pd.DataFrame(car_data)

car_spec_df = pd.DataFrame.from_dict(car_spec, orient="index").reset_index()
car_spec_df.rename(columns={"index": "centralVariantId"}, inplace=True)

# Merge with car_data
merged_df = car_data_df.merge(car_spec_df, on="centralVariantId", how="inner")

# Save file into csv
merged_df.to_csv("cardekho.csv", index=False)