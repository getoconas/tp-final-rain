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
from .the_conversation import get_article_theconversation
from .noticias_caracol import get_article_noticiascaracol
from .wired import get_article_wired
from .el_tribuno import get_article_eltribuno
from .efe import get_article_efe

ALL_ARTICLES = {
  'somosjujuy': get_article_somosjujuy,
  'pagina12': get_article_pagina12,
  'elpais': get_article_elpais,
  'euronews': get_article_euronews,
  'quepasajujuy': get_article_quepasajujuy,
  'jujuydice': get_article_jujuydice,
  'tn': get_articles_tn,
  'conicet': get_article_conicet,
  'sinc': get_article_sinc,
  'muycomputer': get_article_muycomputer,
  'theconversation': get_article_theconversation,
  'caracol': get_article_noticiascaracol,
  'wired': get_article_wired,
  'eltribuno': get_article_eltribuno,
  'efe': get_article_efe
}
