import unicodedata

def clean_and_lower(text):
  text = ''.join(
    c for c in unicodedata.normalize("NFKD", text)
    if unicodedata.category(c) != 'Mn'
  )
  return text.lower()

def clean_text(text):
  text = ''.join(
    c for c in unicodedata.normalize("NFKD", text)
    if unicodedata.category(c) != 'Mn'
  )
  return text