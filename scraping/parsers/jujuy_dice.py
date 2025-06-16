from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_jujuydice(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'jujuy dice': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary_tag = soup.find('p', itemprop="description")
  summary = ''
  if summary_tag:
    summary = summary_tag.find(text=True, recursive=False)
    if summary:
      summary = summary.strip()

  # Contenido
  article_content = soup.find('div', class_='cda')
  content = []
  if article_content:
    for elem in article_content:
      if elem.name == 'p':
        text = elem.get_text()
        if text:
          content.append(text)
    
  text = summary + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
