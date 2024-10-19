# search_engine.py
import requests
from bs4 import BeautifulSoup

class QttpSearchEngine:
    def __init__(self):
        self.engines = {
            'google': 'https://www.google.com/search?q=',
            'bing': 'https://www.bing.com/search?q=',
            'duckduckgo': 'https://duckduckgo.com/?q='
        }

    def search(self, query):
        results = []
        for engine, url in self.engines.items():
            results.extend(self._get_results(url + query, engine))
        return results

    def _get_results(self, search_url, engine):
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        if engine == 'google':
            for g in soup.find_all('h3'):
                links.append(g.text)
        elif engine == 'bing':
            for b in soup.find_all('h2'):
                links.append(b.text)
        elif engine == 'duckduckgo':
            for d in soup.find_all('a', class_='result__a'):
                links.append(d.text)
        
        return links
