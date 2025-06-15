from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_conicet(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'conicet': {response.status_code}")
    return []

  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1')
  title = title.get_text(strip=True) if title else ''

  # Resumen
  summary_tag = soup.find('div', class_="title-description")
  if summary_tag:
    for elem in summary_tag:
      if elem.name == 'p' and 'volanta-single' not in elem.get('class', []):
        summary = elem.get_text()
        if len(summary) > 0:
          summary_final = summary

  # Contenido
  article_content = soup.find('div', class_='detalle-cuerpo')
  content = []
  if article_content:
    article_text_div = article_content.find('div', class_='resize')
    if article_text_div:
      for elem in article_text_div:
        if elem.name == 'p':
          text = elem.get_text()
          if text:
            content.append(text)

  text = summary_final + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
