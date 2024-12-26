from os.path import split

import requests
from bs4 import BeautifulSoup

def scraper_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('h2', class_='post-title')

        result = [f"Articles Titles:\n"]

        for article in articles:
            result.append(f"{article.get_text(strip=True)}\n")

        return "".join(result)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

web_url = "" # Add your desired web url
print(scraper_articles(web_url))