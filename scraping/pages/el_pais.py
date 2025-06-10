from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_elpais(query, max_news):
  url = f"https://elpais.com/buscador/{quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página: {response.status_code}")
    return []  
  
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('article')
  
  news = []
  for article in articles:
    h2 = article.find('h2', class_=lambda x: x and 'c_t' in x)
    if h2:
      a_tag = h2.find('a')
      if a_tag and a_tag.get('href'):
        title = a_tag.get_text(strip=True)
        url = a_tag['href']
        # Si el enlace es relativo, agregar el dominio
        if url.startswith('/'):
          url = 'https://elpais.com' + url
        news.append({'titulo': title, 'enlace': url})
        if len(news) >= max_news:
          break

  return news