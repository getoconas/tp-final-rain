from scraping.pages.somos_jujuy import get_news_somosjujuy
from scraping.pages.pagina_12 import get_news_pagina12
from scraping.pages.el_pais import get_news_elpais
from scraping.pages.euronews import get_news_euronews
from scraping.pages.que_pasa_jujuy import get_news_quepasajujuy
from scraping.pages.jujuy_dice import get_news_jujuydice
from scraping.pages.tn import get_news_tn

# Programa principal
if __name__ == "__main__":
  print(get_news_elpais("lento", 10))
  