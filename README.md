# Web Scraper Challenge

The challenge is to scrape quotes off the many different website design styles. It is based on the website http://toscrape.com/ which allows users to freely scrape its website to learn and challenge themselves.

The scraper will extract all the quotes and authors and write it to a csv file.

Sample csv file [here](quotes.csv)

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
- Pandas

## Usage

1. Scraping the default website

```bash
python3 default.py
```

2. Scraping the infinite scrolling website

```bash
python3 scroll.py
```

3. Scraping the javascript rendered website 

```bash
python3 javascript.py
```

4. Scraping the table based messed-up layout website

```bash
python3 tableful.py
```

5. Scraping the login website

```bash
python3 login.py
```

6. Scraping the AJAX based filter form with ViewStates website

```bash
python3 viewstate.py
```

7. Scraping the random generated quote website

```bash
python3 random.py
```
