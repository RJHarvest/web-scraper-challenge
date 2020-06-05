import os
import csv
import requests
import numpy as np
from bs4 import BeautifulSoup

def scrape():
    html_page = requests.get('http://quotes.toscrape.com/')
    content = html_page.content
    soup = BeautifulSoup(content, 'html.parser')

    quote_elements = soup.find_all('span', class_='text')
    author_elements = soup.find_all('small', class_='author')
    
    quotes = [quote.text for quote in quote_elements]
    authors = [author.text for author in author_elements]

    quote_data = np.column_stack((quotes, authors))

    return quote_data

def storeToCsv(quotes):
    header = ['quotes', 'authors']
    with open('default.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(quotes)

def main():
    # step 1: scrape website
    quotes = scrape()
    # step 2: store data to csv file
    storeToCsv(quotes)

if __name__ == '__main__':
    main()
