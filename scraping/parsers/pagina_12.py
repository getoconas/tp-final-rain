from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_pagina12(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'pagina 12': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('h2', class_="h3 ff-20px-w400")
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('div', class_='section-2-col article-main-content')
  content = []
  if article_content:
    article_text_div = article_content.find('div', class_='article-main-content article-text')
    if article_text_div:
      for elem in article_text_div:
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
