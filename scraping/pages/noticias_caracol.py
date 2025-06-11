from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_caracol(query, max_news):
  url = f"https://www.noticiascaracol.com/busqueda?q={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'noticias caracol': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('li', class_='SearchResultsModule-results-item')
  
  news = []
  for article in articles:
    a_tag = article.find('a')
    if a_tag and a_tag.get('href'):
      title = a_tag.get('title', '').strip()
      url = a_tag['href']
      if not url.startswith('http'):
        url = 'https://www.noticiascaracol.com' + url
      news.append({'titulo': title, 'enlace': url})
      if len(news) >= max_news:
        break
  
  return news
