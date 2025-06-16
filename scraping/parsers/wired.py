from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_wired(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'wired': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('div', class_='ContentHeaderDek-bIqFFZ jTjywE')
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find_all('div', class_='BodyWrapper-kufPGa erMawQ body body__container article__body')
  content = []
  if article_content:
    article_tag = soup.find('div', class_='body__inner-container')
    for elem in article_tag:
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
