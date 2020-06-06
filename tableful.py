import requests
import pandas as pd
from bs4 import BeautifulSoup

# The website is arranged in a badly designed table format
# The quotes and authors are in every alternate table row
# The first table row consists of the side tags
# The last table row consists of the "next" button

def main():
    all_quotes = []
    all_authors = []

    for i in range(1,11):
        html_page = requests.get(f'http://quotes.toscrape.com/tableful/page/{i}')
        content = html_page.content
        soup = BeautifulSoup(content, 'lxml')

        table_rows = soup.find_all('tr')

        quotes = []
        authors = []

        for i in range(1, len(table_rows) - 1, 2):
            text = table_rows[i].text.split('Author:')

            quotes.append(text[0].strip())
            authors.append(text[1].strip())

        all_quotes.extend(quotes)
        all_authors.extend(authors)

    df = pd.DataFrame({
        'quotes': all_quotes,
        'authors': all_authors
    })
    df.to_csv('quotes.csv', index=False)

if __name__ == '__main__':
    main()
