from utils import RDW_ENDPOINT
import requests
from typing import List, Dict

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


def my_func(x, *args, **kwargs):
    pass