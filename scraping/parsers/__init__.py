from .somos_jujuy import get_article_somosjujuy
from .pagina_12 import get_article_pagina12
from .el_pais import get_article_elpais
from .euronews import get_article_euronews
from .que_pasa_jujuy import get_article_quepasajujuy
from .jujuy_dice import get_article_jujuydice

ALL_ARTICLES = [
  get_article_somosjujuy,
  get_article_pagina12,
  get_article_elpais,
  get_article_euronews,
  get_article_quepasajujuy,
  get_article_jujuydice
]
