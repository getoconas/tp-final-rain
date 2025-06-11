from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_canal26(query, max_news):
  url = f"https://www.canal26.com/buscar?palabra={quote(query)}"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'canal 26': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('div', class_='listing_article_medium group relative')
 
  news = []
  for article in articles:
    a_tag = article.find('a')
    h2 = article.find('h2', class_='listing_article_medium_title')
    if a_tag and a_tag.get('href'):
      title = h2.get_text(strip=True)
      url = a_tag['href']
      if url.startswith('/'):
        url = "https://www.canal26.com" + url
      news.append({'titulo': title, 'enlace': url})
      if len(news) >= max_news:
        break

  return news
