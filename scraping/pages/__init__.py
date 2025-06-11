from .somos_jujuy import get_news_somosjujuy
from .pagina_12 import get_news_pagina12
from .el_pais import get_news_elpais
from .euronews import get_news_euronews
from .que_pasa_jujuy import get_news_quepasajujuy
from .jujuy_dice import get_news_jujuydice
from .tn import get_news_tn

ALL_NEWS = [
  get_news_somosjujuy,
  get_news_pagina12,
  get_news_elpais,
  get_news_euronews,
  get_news_quepasajujuy,
  get_news_jujuydice,
  get_news_tn
]