import json
import hashlib
from pathlib import Path

def get_cache_path(query):
  base_dir = Path(__file__).parent
  cache_dir = base_dir / "cached_searches"
  cache_dir.mkdir(parents=True, exist_ok=True)
  query_hash = hashlib.md5(query.lower().encode()).hexdigest()
  return Path(cache_dir) / f"{query_hash}.json"

def load_cache(query):
  try:
    with open(get_cache_path(query), 'r', encoding='utf-8') as f:
      return json.load(f)
  except FileNotFoundError:
    return None
  except json.JSONDecodeError: # Añadir manejo para archivos JSON corruptos o vacíos
    print(f"Advertencia: El archivo de caché para '{query}' está corrupto o vacío.")
    return None

def save_cache(query, data):
  with open(get_cache_path(query), 'w', encoding='utf-8') as f: # Añadir encoding para evitar errores
    json.dump(data, f, ensure_ascii=False, indent=2)
