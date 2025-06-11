from scraping.pages import ALL_NEWS

# Programa principal
if __name__ == "__main__":

  all_articles = []
  for get_news in ALL_NEWS:
    try:
      news = get_news("inteligencia artificial", 10) 
      all_articles.extend(news)
      print(f"{get_news.__name__} finalizado. Noticias obtenidas: {len(news)}")
    except Exception as e:
      print(f"Error al procesar {get_news.__name__}: {e}")
