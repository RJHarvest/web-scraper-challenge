# Web Scraper Challenge

The challenge is to scrape quotes off the many different website design styles. It is based on the website http://toscrape.com/ which allows users to freely scrape its website to learn and challenge themselves.

### Website styles

- Default: Simple website with microdata and pagination
  - http://quotes.toscrape.com/
- Scoll: Website with infinite scroll pagination 
  - http://quotes.toscrape.com/scroll
- JavaScript: A JavaScript generated content website
  - http://quotes.toscrape.com/js
- Tableful: A website with a table based messed-up layout 
  - http://quotes.toscrape.com/tableful
- Login: A login website with CSRF token
  - http://quotes.toscrape.com/login
- ViewState: An AJAX based filter form with ViewStates 
  - http://quotes.toscrape.com/search.aspx
- Random: Website that produces a single random quote
  - http://quotes.toscrape.com/random

## Prerequisites

- Python 3.6+
- BeautifulSoup

## Usage

1. Scraping the default website

Sample csv file [here](csv/default.csv)

```bash
python3 default.py
```
