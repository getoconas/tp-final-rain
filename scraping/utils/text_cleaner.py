import unicodedata
import re

def clean_text(text):
  text = re.sub(r'\s+', ' ', text) # Reemplaza uno o más espacios/saltos de línea por un solo espacio

  # Patrones para reemplazar por comillas dobles
  quote_patterns = ['‘', '’', '“', '”', '«', '»', '\x93', '\x94', '\'']
  text = re.sub(r'|'.join(map(re.escape, quote_patterns)), '"', text)

  # Normalización Unicode para acentos
  text = unicodedata.normalize("NFKC", text)
  text = ''.join(c for c in text if not unicodedata.category(c) == 'Mn')
  
  return text.strip() # Añadir .strip() para limpiar espacios al principio/final
