import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_news_pagina12(query, max_news):
  url = f"https://www.pagina12.com.ar/buscar?q={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página: {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('article', class_='article-item article-item--teaser')

  news = []
  for article in articles:
    h4 = article.find('h4', class_='title is-display-inline ff-22px-w700-ls-07')
    if h4:
      a_tag = h4.find('a')
      if a_tag and a_tag.get('href'):
        titulo = a_tag.get_text(strip=True)
        enlace = a_tag['href']
        if enlace.startswith('/'):
          enlace = 'https://www.pagina12.com.ar' + enlace
        news.append({'titulo': titulo, 'enlace': enlace})
        if len(news) >= max_news:
          break

  return news