import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    html_page = requests.get('http://quotes.toscrape.com/')
    content = html_page.content
    soup = BeautifulSoup(content, 'html.parser')

    quote_elements = soup.find_all('span', class_='text')
    author_elements = soup.find_all('small', class_='author')
    
    quotes = [quote.text for quote in quote_elements]
    authors = [author.text for author in author_elements]

    quote_data = pd.DataFrame({
        'quotes': quotes,
        'authors': authors
    })
    quote_data.to_csv('default.csv', index=False)

if __name__ == '__main__':
    main()
