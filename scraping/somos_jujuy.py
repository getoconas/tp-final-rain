import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_news_somosjujuy(query, max_news):
  url = f"https://www.somosjujuy.com.ar/search?q={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página: {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')
  h2_tags = soup.find_all('h2', class_='tit')

  news = []
  for h2 in h2_tags:
    a_tag = h2.find('a')
    if a_tag and a_tag.get('href'):
      title = a_tag.get_text(strip=True)
      url = a_tag['href']
      news.append({'titulo': title, 'enlace': url})
      if len(news) >= max_news:
        break

  return news