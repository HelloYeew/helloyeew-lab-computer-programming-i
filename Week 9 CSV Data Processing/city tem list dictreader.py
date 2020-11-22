import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
# city = []
# temp = []
# for i in range(len(cities_data)):
#     city.append(cities_data[i]['city'])
# for i in range(len(cities_data)):
#     temp.append(float(cities_data[i]['temperature']))
# print(city)
# print(temp)
city_temp_tuple = []
for i in range(len(cities_data)):
    append_tuple = (cities_data[i]['city'], float(cities_data[i]['latitude']))
    city_temp_tuple.append(append_tuple)
print(city_temp_tuple)