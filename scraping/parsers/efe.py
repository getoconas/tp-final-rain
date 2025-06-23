from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_efe(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'efe': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1', class_='entry-title')
  title = title.get_text() if title else ''
  title = clean_text(title)

  # Contenido
  article_content = soup.find('div', class_='entry-content')
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
  
  text = ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
