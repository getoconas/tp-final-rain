from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_tn(query, max_news):
    url = f"https://tn.com.ar/buscar/{quote(query)}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error al obtener la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='card__container card__horizontal')

    news = []
    for article in articles:
      a_tag = article.find('a')
      if a_tag and a_tag.get('href'):
        title = a_tag.get_text(strip=True)
        url = a_tag['href']
        # Si el enlace es relativo, agregar el dominio
        if url.startswith('/'):
          url = 'https://tn.com.ar' + url
        news.append({'titulo': title, 'enlace': url})
        if len(news) >= max_news:
          break

    return news
