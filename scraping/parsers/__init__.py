from .somos_jujuy import get_article_somosjujuy
from .pagina_12 import get_article_pagina12
from .el_pais import get_article_elpais
from .euronews import get_article_euronews
from .que_pasa_jujuy import get_article_quepasajujuy
from .jujuy_dice import get_article_jujuydice
from .tn import get_articles_tn
from .conicet import get_article_conicet
from .sinc import get_article_sinc
from .muy_computer import get_article_muycomputer

ALL_ARTICLES = [
  get_article_somosjujuy,
  get_article_pagina12,
  get_article_elpais,
  get_article_euronews,
  get_article_quepasajujuy,
  get_article_jujuydice,
  get_articles_tn,
  get_article_conicet,
  get_article_sinc,
  get_article_muycomputer
]
