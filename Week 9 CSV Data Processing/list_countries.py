import csv

def list_countries(data):
    countries = []
    for row in data:
        country = row['country']
        if country not in countries:
            countries.append(country)
    return countries

cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
countries = list_countries(cities_data)
print(len(countries))
print(countries)