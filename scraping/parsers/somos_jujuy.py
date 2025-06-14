from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_somosjujuy(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'somos jujuy': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # Titulo de la noticia
  title = soup.find('h1', class_='tit-ficha')
  title = title.get_text(strip=True) if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('h2', class_='sufix-ficha')
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('article', class_='content')
  content = []
  if article_content:
    col_div = article_content.find('div', class_='col')
    if col_div:
      for elem in col_div.children:
        if elem.name == 'p':
          text = elem.get_text()
          if text:
            content.append(text)
        elif elem.name == 'h4':
          text = elem.get_text(strip=True)
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
