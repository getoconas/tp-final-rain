from scraping.runner import get_all_news, fetch_articles_content

# Programa principal
if __name__ == "__main__":
  query = "eclipse"
  max_news = 10

  print("📡 Obteniendo enlaces de noticias...")
  news = get_all_news(query, max_news)

  print(f"\n🔎 Total noticias encontradas: {len(news)}. Comenzando la extracción de contenido...\n")
  all_articles = fetch_articles_content(news)

  print(f"\n✅ Artículos completos extraídos: {len(all_articles)}")

  if all_articles:
    print(all_articles)
  