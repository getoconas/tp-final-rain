import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity

spanish_stopwords = stopwords.words('spanish') # Cargar stopwords

# Entrena el modelo TF-IDF + LSI
def train_model(data_articles):
  pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=spanish_stopwords)),
    ('lsi', TruncatedSVD(n_components=100))
  ])
  corpus = [article['titulo'] + " " + article['contenido'] for article in data_articles] 
  pipeline.fit(corpus)
  doc_vecs = pipeline.transform(corpus) 
  return pipeline, doc_vecs

# Buscar artículos utilizando el modelo entrenado y los vectores de documentos. Recibe la consulta, el modelo entrenado (pipeline) y los vectores de los documentos.
def search(query, model, data_articles_doc_vecs):
  # Transformar la consulta en un vector usando el modelo entrenado
  query_vec = model.transform([query])
  
  # Calcular la similitud del coseno entre la consulta y los vectores de los documentos
  scores = cosine_similarity(query_vec, data_articles_doc_vecs).flatten() 
  return scores
