import unicodedata

def clean_text(text):
  text = text.replace('  ',' ').replace('   ','').replace('“','"').replace('”','"').replace('«','"').replace('»','"').replace('\x93','"').replace('\x94','"').replace('\'','"').replace('\n',' ')
  text = unicodedata.normalize("NFKC", text)
  return text