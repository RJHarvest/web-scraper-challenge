import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup

# The website uses CSRF to login users
# The website form data includes:
#   - username
#   - password
#   - csrf_token (hidden)
# The website allows any username and password combination
# Note: It does not authenticate empty username and password

def login():
    login_url = 'http://quotes.toscrape.com/login'
    payload = {
        'username': 'test',
        'password': 'test',
        'csrf_token': 'gRKEqnVUDCSutfbLMWFBiwohczTJOslmNGpajvXHZPyxdkIAYeQr'
    }

    session_requests = requests.session()
    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

    # send post request to authenticate user before scraping
    result = session_requests.post(
	login_url,
	data = payload,
	headers = dict(referer=login_url)
    )

    if (not result.ok):
        return False
    return session_requests

def scrape(session_requests):
    all_quotes = []
    all_authors = []

    for i in range(1,11):
        quotes_url = f'http://quotes.toscrape.com/page/{i}'
        # scrape quote website
        html_page = session_requests.get(
	    quotes_url,
	    headers = dict(referer=quotes_url)
        )
        content = html_page.content
        soup = BeautifulSoup(content, 'lxml')

        quote_elements = soup.find_all('span', class_='text')
        author_elements = soup.find_all('small', class_='author')

        quotes = [quote.text for quote in quote_elements]
        authors = [author.text for author in author_elements]

        all_quotes.extend(quotes)
        all_authors.extend(authors)

    df = pd.DataFrame({
        'quotes': all_quotes,
        'authors': all_authors
    })
    df.to_csv('quotes.csv', index=False)

def main():
    # step 1: login user
    session = login()
    # step 2: scrape website content
    if (not session):
        print('Invalid Authentication')
        return
    scrape(session)

if __name__ == '__main__':
    main()
