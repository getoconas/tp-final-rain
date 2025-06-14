from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_euronews(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'euronews': {response.status_code}")
    return []
  
  response.encoding = response.apparent_encoding
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1', class_='c-article-redesign-title')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('h2', class_='c-article-summary')
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('div', class_='c-article-content js-article-content poool-content')
  content = []
  if article_content:
    for elem in article_content:
      if elem.name == 'p':
        text = elem.get_text()
        if text:
          content.append(text)
      elif elem.name == 'h2':
          text = elem.get_text(strip=True)
          if text:
            content.append(text + ' ')

  text = summary + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
