import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.reader(f)
    for r in rows:
        cities_data.append(r)
city = []
temp = []
for i in range(1,len(cities_data)):
    city.append(cities_data[i][1])
for i in range(1,len(cities_data)):
    temp.append(cities_data[i][6])
print(city)
print(temp)