import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    all_quotes = []
    all_authors = []

    for i in range(1,11):
        html_page = requests.get(f'http://quotes.toscrape.com/page/{i}/')
        content = html_page.content
        soup = BeautifulSoup(content, 'html.parser')

        quote_elements = soup.find_all('span', class_='text')
        author_elements = soup.find_all('small', class_='author')

        quotes = [quote.text for quote in quote_elements]
        authors = [author.text for author in author_elements]

        all_quotes.extend(quotes)
        all_authors.extend(authors)

    quote_data = pd.DataFrame({
        'quotes': all_quotes,
        'authors': all_authors
    })
    quote_data.to_csv('csv/default.csv', index=False)

if __name__ == '__main__':
    main()
