from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_efe(query, max_news):
  url = f"https://efe.com/?s={quote(query)}"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'efe': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('article')
 
  news = []
  for article in articles:
    h2 = article.find('h2', class_='entry-title')
    if h2:
      a = h2.find('a', href=True)
      if a:
        titulo = a.get_text(strip=True)
        enlace = a['href']
        news.append({'titulo': titulo, 'enlace': enlace})
        if len(news) >= max_news:
          break

  return news
