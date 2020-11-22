import csv

def list_countries(data):
    countries = []
    for row in data:
        country = row['country']
        if country not in countries:
            countries.append(country)
    return countries

def compute_ave_country_temp(data):
    ans = {}
    countries = list_countries(data)
    avg_temp = []
    for i in range(len(countries)):
        temp = []
        for j in range(len(data)):
            if data[j]['country'] == countries[i]:
                temp.append(float(data[j]['temperature']))
        avg_temp.append(sum(temp)/len(temp))
    for i in range(len(countries)):
        ans.update({countries[i]: avg_temp[i]})
    return ans

cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
country_temps = compute_ave_country_temp(cities_data)
print(len(country_temps))
print(country_temps)