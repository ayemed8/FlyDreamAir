import pandas as pd
from app.utils.paths import get_international_csv_path

def read_csv(csv_name, column_name):
    data = pd.read_csv(csv_name)
    column_list = data[column_name].to_list()
    return column_list

def get_country_info():
    countries = read_csv(csv_name=get_international_csv_path(), column_name="Country")
    cities = read_csv(csv_name=get_international_csv_path(), column_name="City")
    city_codes = read_csv(csv_name=get_international_csv_path(), column_name="Code")

    all = []
    for country, city, c_code in zip(countries, cities, city_codes):
        all.append(f"{city} - {country} [{c_code}]")   

    return sorted(all)