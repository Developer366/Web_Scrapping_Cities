import requests
from bs4 import BeautifulSoup
import csv

# get url and create soup
url = "https://worldpopulationreview.com/world-cities"
get_url = requests.get(url)
soup = BeautifulSoup(get_url.text, "html.parser") # document ready to be parsed
#print(soup)

# creating the csv file
filename = "cities.csv"
csv_writer = csv.writer(open(filename, 'w', newline='')) # no empty row after inserting

# extracting table data to store in the csv
for tr in soup.find_all('tr'): # for every table row in soup
    data=[]

# scraping table headers first
    for th in tr.find_all('th'):
        data.append(th.text)
    if(data):
        print("Inserting Headers: {}".format(', '.join(data)))
        csv_writer.writerow(data)
        continue

# for scraping the actual table data values

    for td in tr.find_all("td"):
        data.append(td.text)
    if(data):
        print("Inserting Table Data")
        csv_writer.writerow(data)
