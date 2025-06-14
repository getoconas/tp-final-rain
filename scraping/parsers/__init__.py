from .somos_jujuy import get_article_somosjujuy
from .pagina_12 import get_article_pagina12
from .el_pais import get_article_elpais

ALL_ARTICLES = [
  get_article_somosjujuy,
  get_article_pagina12,
  get_article_elpais
]
