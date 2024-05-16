# add a constant for the RDW endpoint
RDW_ENDPOINT = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

# define the default columns
DEFAULT_COLUMNS = ['merk', 'handelsbenaming', 'aantal_cilinders', 
                   'catalogusprijs', 'datum_tenaamstelling']

# default column renaming
DEFAULT_COLUMN_NAMES = {"handelsbenaming": "model",
                        "datum_tenaamstelling": "datum"}