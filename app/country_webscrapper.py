from bs4 import BeautifulSoup
import urllib.request as requests
import pandas as pd
import csv

url = 'https://developers.google.com/public-data/docs/canonical/countries_csv'
url_data = pd.read_html(url)

sauce = requests.urlopen(url).read()
soup = BeautifulSoup(sauce, 'lxml')
soup.prettify()
country_data = soup.find_all('td')

country_list = [c.text for c in country_data]

country_header = ['Country Code', 'Latitude', 'Longitude', 'Country Name']


with open('./countries_list.csv', 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=country_header)
    csv_writer.writeheader()

with open('./countries_list.csv', 'a') as d:
    start = 0
    end = 4
    j = 0
    while j < 245:
        for j in range(0, int(len(country_list)/4)):
            country_code = country_list[start:end][0]
            latitude = country_list[start:end][1]
            longitude = country_list[start:end][2]
            country_name = country_list[start:end][3]
            d.writelines(f'{country_code}, {latitude}, {longitude}, {country_name}')
            d.writelines('\n')
            start += 4
            end += 4
        j += 5
