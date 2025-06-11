from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_pagina12(query, max_news):
  url = f"https://www.pagina12.com.ar/buscar?q={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'página 12': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('article', class_='article-item article-item--teaser')

  news = []
  for article in articles:
    h4 = article.find('h4', class_='title is-display-inline ff-22px-w700-ls-07')
    if h4:
      a_tag = h4.find('a')
      if a_tag and a_tag.get('href'):
        title = a_tag.get_text(strip=True)
        url = a_tag['href']
        if url.startswith('/'):
          url = 'https://www.pagina12.com.ar' + url
        news.append({'titulo': title, 'enlace': url})
        if len(news) >= max_news:
          break

  return news
