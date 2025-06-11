from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_eltribuno(query, max_news):
  url = f"https://eltribunodejujuy.com/b/{quote(query)}"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'el tribuno': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('article', class_='nota nota--linea')

  news = []
  for article in articles:
    a_tag = article.find('a')
    if a_tag and a_tag.get('href'):
      title = a_tag.get('aria-label', '').strip()
      url = a_tag['href']
      if url.startswith('/'):
        url = "https://eltribunodejujuy.com" + url
      news.append({'titulo': title, 'enlace': url})
      if len(news) >= max_news:
        break

  return news
