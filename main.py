from utils.import_functions import import_car_brand
from utils.conversion_functions import convert_clean_list_to_df

import argparse

# (1/3) create an argument parser
parser = argparse.ArgumentParser()

# (2/3) add arguments to the parser
parser.add_argument("--brand", "-b",
                    type=str,
                    required=False,
                    help="Specify the brand of the car")

parser.add_argument("--export", "-e",
                    type=str, 
                    choices=["print", "csv", "db"],
                    default="print",
                    help="Indicate how to export the data. (default 'print')"
                    )


# (3/3) parse the args
args = parser.parse_args()

# access the arguments
selected_brand = args.brand
selected_export = args.export


# import the car data
cars_list = import_car_brand(selected_brand)

# conver the list to a pandas DataFrame
cars_df = convert_clean_list_to_df(cars_list,  "aantal_zitplaatsen", "voertuigsoort",
                                   handelsbenaming="modelnaam",
                                   aantal_zitplaatsen="zitplaatsen",
                                   voertuigsoort="type")

if selected_export == "print":
    print(cars_df.head())
elif selected_export == "csv":
    print("Exporting to csv")
else:
    print("Writing to db")