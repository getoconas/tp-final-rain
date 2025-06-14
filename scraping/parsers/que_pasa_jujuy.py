from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_quepasajujuy(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'que pasa jujuy': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1', class_='title content-title')
  title = title.get_text(strip=True) if title else ''
  # Resumen
  summary = soup.find('h2', class_='description')
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('div', class_='background')
  content = []
  if article_content:
    article_text_div = article_content.find('div', class_='content vsmcontent')
    if article_text_div:
      for elem in article_text_div:
        if elem.name == 'p':
          text = elem.get_text()
          if text:
            content.append(text)
        elif elem.name == 'h3':
          text = elem.get_text()
          if text:
            content.append(text + ' ')
        elif elem.name == 'ul':
          for li in elem.find_all('li'):
            li_text = li.get_text(strip=True)
            if li_text:
              content.append('- ' + li_text)

  text = summary + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
