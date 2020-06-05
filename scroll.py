import requests
import pandas as pd

# The infinite scroll page sends AJAX request to API to get quotes
# The AJAX response is a JSON object

def main():
    all_quotes = []
    all_authors = []

    for i in range(1,11):
        html_page = requests.get(f'http://quotes.toscrape.com/api/quotes?page={i}')
        json_response = html_page.json()

        quote_obj = json_response['quotes']
        quotes = [quote['text'] for quote in quote_obj]
        authors = [quote['author']['name'] for quote in quote_obj]

        all_quotes.extend(quotes)
        all_authors.extend(authors)

    df = pd.DataFrame({
        'quotes': all_quotes,
        'authors': all_authors
    })
    df.to_csv('quotes.csv', index=False)

if __name__ == '__main__':
    main()
