#from utils import RDW_ENDPOINT
import requests
from typing import List, Dict

RDW_ENDPOINT = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

def import_car_brand(brand: str) -> List[Dict]:
    '''
    Function to import cars from the RDW by its brand

    Input:
    * brand: name of the car brand
    
    '''
    
    # uppercase the brand
    brand_upper = brand.upper()

    # compose the endpoint
    endpoint = f"{RDW_ENDPOINT}?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    return data


if __name__ == "__main__":
    selected_brand = input("Insert brand:\n")

    cars_list = import_car_brand(selected_brand)

    print(cars_list)



pass