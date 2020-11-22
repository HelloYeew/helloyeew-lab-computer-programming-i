# P1
# 1.1
import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.reader(f)
    for r in rows:
        cities_data.append(r)
print(cities_data[0:10])
print(cities_data[8:10])

# 1.2
import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
print(cities_data[0:10])
print(cities_data[8:10])

# DictReader print as dictionary and not print the first row but reader print as list and print a first row
# Choose DictReader

# P2
import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
city_temp_tuple = []
for i in range(len(cities_data)):
    append_tuple = (cities_data[i]['city'], float(cities_data[i]['latitude']))
    city_temp_tuple.append(append_tuple)
print(city_temp_tuple)

# P3
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

# P4
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

# P5
import csv
import matplotlib.pyplot as plt

def read_file(file_name):
    data = []
    with open(file_name, 'r', encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            data.append(r)
    return data

def extract_to_list(data,type):
    ans = []
    for row in data:
        row_value = row[type]
        ans.append(row_value)
    for i in range(len(ans)):
        ans[i] = float(ans[i])
    return ans

cities_data = read_file('cities.csv')
lat = extract_to_list(cities_data,'latitude')
long = extract_to_list(cities_data,'longitude')
temps = extract_to_list(cities_data,'temperature')
high = extract_to_list(cities_data,'highest')
# Plot scatter plot using x = latitude,
#                         y = temperature,
#                         color=longitude
plt.scatter(lat,temps,c=long)
# Add x-axis label
plt.xlabel('Latitude')
# Add y-axis label
plt.ylabel('Temperatures')
# Add label for color bar
plt.colorbar().ax.set_title('Longtitude')
# Save plot as image file
plt.savefig('lat_temps_long.png')
# Show plot
plt.show()

plt.scatter(long,temps,c=lat)
plt.xlabel('Longitude')
plt.ylabel('Temperatures')
plt.colorbar().ax.set_title('Latitude')
# Set colormap to the selected one
# See more colormap selection in the reference at the end of Exercise 5
plt.set_cmap('RdBu')
plt.savefig('long_temps_lat.png')
plt.show()

# P6

import csv
import matplotlib.pyplot as plt

def read_file(file_name):
    data = []
    with open(file_name, 'r', encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            data.append(r)
    return data

def extract_to_list(data,type):
    ans = []
    for row in data:
        row_value = row[type]
        ans.append(row_value)
    for i in range(len(ans)):
        ans[i] = float(ans[i])
    return ans

def count_region_freq(data):
    region = []
    freq = []
    for i in range(len(data)):
        if data[i]["region"] not in region:
            region.append(data[i]["region"])
    for i in range(len(region)):
        append_freq = 0
        for j in range(len(data)):
            if region[i] == data[j]["region"]:
                append_freq += 1
        freq.append(append_freq)
    return region,freq

cities_data = read_file('cities.csv')
region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
#                      y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()

# P7

def find_lowest_highest_avg_city_temp(data):
    countries = []
    cities = []
    avg_temp = []
    for row in data:
        country = row['country']
        if country not in cities:
            countries.append(country)
    for i in range(len(countries)):
        append_city_list = []
        for j in range(len(data)):
            if data[j]["country"] == countries[i]:
                append_city_list.append(data[j]["city"])
        cities.append(append_city_list)
    for i in range(len(cities)):
        city_temp_for_avg = []
        for j in range(len(cities[i])):
            for k in range(len(data)):
                if data[k]["city"] == cities[i][j]:
                    city_temp_for_avg.append(float(data[k]["temperature"]))
        avg_temp.append(sum(city_temp_for_avg)/len(city_temp_for_avg))
    max_country = countries[avg_temp.index(max(avg_temp))]
    min_country = countries[avg_temp.index(min(avg_temp))]
    return [min_country,max_country]

# P8
import csv
import matplotlib.pyplot as plt

def read_file(file_name):
    data = []
    with open(file_name, 'r', encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            data.append(r)
    return data

def compute_ave_region_highest(data):
    region = []
    avg_highest = []
    for i in range(len(data)):
        if data[i]['region'] not in region:
            region.append(data[i]['region'])
    for i in range(len(region)):
        for_avg_highest = []
        for j in range(len(data)):
            if data[j]['region'] == region[i]:
                for_avg_highest.append(float(data[j]['highest']))
        avg_highest.append(sum(for_avg_highest)/len(for_avg_highest))
    return region,avg_highest

cities_data = read_file('cities.csv')
region_list, average_highest_list = compute_ave_region_highest(cities_data)
# Set up bar colors in bar graph
my_colors = ['thistle','pink','tan','slateblue']
# Plot bar graph using x = unique region list
#                      y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, average_highest_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Average Highest')
plt.savefig('average_highest.png')
plt.show()