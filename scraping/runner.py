from concurrent.futures import ThreadPoolExecutor, as_completed

from scraping.pages import ALL_NEWS
from scraping.parsers import ALL_ARTICLES

def get_all_news(query, max_news):
  articles = []

  for get_news in ALL_NEWS:
    try:
      news = get_news(query, max_news)
      for item in news:
        item['parser_name'] = get_news.__name__.replace("get_news_", "")
      articles.extend(news)
      print(f"✅ {get_news.__name__} finalizado. Noticias obtenidas: {len(news)}")
    except Exception as e:
      print(f"❌ Error en {get_news.__name__}: {e}")

  return articles

def fetch_articles_content(news_list):
  full_articles = []

  def fetch(article):
    parser = ALL_ARTICLES.get(article['parser_name'])
    if not parser:
      print(f"❌ Parser no encontrado para {article['parser_name']}")
      return None
    try:
      content = parser(article['enlace'])
      if content:
        return {
          'titulo': content['titulo'],
          'contenido': content['contenido'],
          'enlace': article['enlace']
        }
    except Exception as e:
      print(f"Error en parser {parser.__name__}: {e}")
      return None

  with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch, art) for art in news_list]
    for future in as_completed(futures):
      result = future.result()
      if result:
        full_articles.append(result)

  return full_articles
