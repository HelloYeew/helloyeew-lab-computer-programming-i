import csv
import matplotlib.pyplot as plt

def read_file(file):
    cities_data = []
    with open(file, 'r', encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            cities_data.append(r)
    return cities_data

def extract_to_list(data,type):
    lst = []
    for i in range(len(data)):
        lst.append(data[i][type])
    return lst


cities_data = read_file('cities.csv')
lat = extract_to_list(cities_data,'latitude')
long = extract_to_list(cities_data,'longitude')
temps = extract_to_list(cities_data,'temperature')
high = extract_to_list(cities_data,'highest')
# Plot scatter plot using x = latitude,
#                         y = temperature,
# color=longitude
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