import csv
import matplotlib.pyplot as plt

def read_file(file_name):
    data = []
    with open(file_name, 'r', encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            data.append(r)
    return data

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



cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
print(find_lowest_highest_avg_city_temp(cities_data[:11]))
print(find_lowest_highest_avg_city_temp(cities_data[-10:]))
print(find_lowest_highest_avg_city_temp(cities_data))
print(compute_ave_region_highest(cities_data))

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