from scraping.utils.common import requests, BeautifulSoup, quote

def get_news_wired(query, max_news):
  url = f"https://es.wired.com/search?q={quote(query)}"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"Error al obtener la página 'wired': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('div', class_='SummaryItemContent-eiDYMl dogWHS summary-item__content')

  news = []
  for article in articles:
    a_tag = article.find('a', class_='SummaryItemHedLink-civMjp hAREyO summary-item-tracking__hed-link summary-item__hed-link')
    if a_tag:
      title_tag = a_tag.find('h2', class_='SummaryItemHedBase-hiFYpQ jUdHzd summary-item__hed')
      if title_tag:
        title = title_tag.get_text(strip=True)
        url = a_tag['href']
        if url.startswith('/'):
          url = 'https://es.wired.com' + url
        news.append({'titulo': title, 'enlace': url})
        if len(news) >= max_news:
          break
  
  return news
