from utils.import_functions import import_car_brand
from utils.conversion_functions import convert_clean_list_to_df

# prompt for the car brand
selected_brand = input("Insert the brand name of the car:\n")

# import the car data
cars_list = import_car_brand(selected_brand)

# conver the list to a pandas DataFrame
cars_df = convert_clean_list_to_df(cars_list,  "aantal_zitplaatsen", "voertuigsoort",
                                   handelsbenaming="modelnaam",
                                   aantal_zitplaatsen="zitplaatsen",
                                   voertuigsoort="type")

print(cars_df.head())