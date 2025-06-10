from scraping.somos_jujuy import get_news_somosjujuy
from scraping.pagina_12 import get_news_pagina12
from scraping.el_pais import get_news_elpais
from scraping.euronews import get_news_euronews
from scraping.que_pasa_jujuy import get_news_quepasajujuy

# Programa principal
if __name__ == "__main__":
  print(get_news_quepasajujuy("libertad", 10))
  