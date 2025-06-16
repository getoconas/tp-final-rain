from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_articles_tn(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'tn': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1', class_='article__title font__display')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('h2', class_="article__dropline font__body")
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('div', class_='default-article-color article__body article__article')
  content = []
  if article_content:
    for elem in article_content:
      if elem.name == 'p':
        if elem.find('b') and 'Leé también:' in elem.find('b').get_text():
          continue 
        text = elem.get_text()
        if text:
          content.append(text)
      elif elem.name == 'h2':
        text = elem.get_text()
        if text:
          content.append(text + ' ')
  
  text = summary + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }        
