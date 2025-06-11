from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_muycomputer(query, max_news):
  url = f"https://www.muycomputer.com/?s={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'muy computer': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('li', class_='mvp-blog-story-wrap left relative infinite-post')

  news = []
  for article in articles:
    a_tag = article.find('a', rel='bookmark')
    h2_tag = article.find('h2')
    if a_tag and h2_tag and a_tag.get('href'):
      title = h2_tag.get_text(strip=True)
      url = a_tag['href']
      news.append({'titulo': title, 'enlace': url})
      if len(news) >= max_news:
        break

  return news
