from scraping.utils.common import requests, BeautifulSoup, clean_text
from scraping.utils.headers import get_random_headers

def get_article_theconversation(url):
  response = requests.get(url, headers=get_random_headers())
  if response.status_code != 200:
    print(f"Error al obtener la noticia de 'the conversation': {response.status_code}")
    return []
  
  soup = BeautifulSoup(response.text, 'html.parser')

  # Titulo de la noticia
  title = soup.find('h1')
  title = title.get_text() if title else ''
  title = clean_text(title)

  # Resumen
  summary = soup.find('figcaption')
  summary = summary.get_text(strip=True) if summary else ''

  # Contenido
  article_content = soup.find('div', itemprop='articleBody')
  content = []
  if article_content:
    for elem in article_content:
      if elem.name == 'p':
        read_more_em_tag = elem.find('em', recursive=False)
        if read_more_em_tag:
          read_more_strong_tag = read_more_em_tag.find('strong', recursive=False)
          if read_more_strong_tag and "Read more:" in read_more_strong_tag.get_text(strip=True):
              read_more_em_tag.extract()
        text = elem.get_text()
        if text:
          content.append(text)
      elif elem.name == 'h2':
        text = elem.get_text(strip=True)
        if text:
          content.append(text + ' ')
      elif elem.name == 'ul':
          for li in elem.find_all('li'):
            li_text = li.get_text()
            if li_text:
              content.append('- ' + li_text)
  
  text = summary + ' ' + '\n'.join(content)
  text = clean_text(text)

  return {
    'titulo': title,
    'contenido': text
  }
