import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json
import pandas as pd
import webbrowser

from scraping.runner import get_all_news, fetch_articles_content
from data.semantic import train_model, search
from data.cache_manager import load_cache, save_cache

class NewsApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Buscador Semántico de Noticias")
    self.setup_ui()
    self.articles = []
    self.model = None
  
  def setup_ui(self):
    # Frame principal
    main_frame = ttk.Frame(self.root, padding="10")
    main_frame.pack(expand=True, fill="both")
    
    # Panel de scraping
    scrape_frame = ttk.LabelFrame(main_frame, text="Fase 1: Obtener Noticias", padding=10)
    scrape_frame.pack(fill="x", pady=5)
    
    ttk.Label(scrape_frame, text="Tema inicial:").grid(row=0, column=0, sticky="w")
    self.scrape_query = ttk.Entry(scrape_frame, width=40)
    self.scrape_query.grid(row=0, column=1, padx=5)
    
    ttk.Button(scrape_frame, text="Scrapear Noticias", command=self.scrape_news).grid(row=0, column=2, padx=5)
    
    # Panel de búsqueda semántica
    search_frame = ttk.LabelFrame(main_frame, text="Fase 2: Búsqueda Semántica", padding=10)
    search_frame.pack(fill="x", pady=5)
    
    ttk.Label(search_frame, text="Consulta:").grid(row=0, column=0, sticky="w")
    self.search_query = ttk.Entry(search_frame, width=40)
    self.search_query.grid(row=0, column=1, padx=5)
    
    ttk.Button(search_frame, text="Buscar", command=self.semantic_search).grid(row=0, column=2, padx=5)
    
    # Sección de Resultados
    results_frame = ttk.LabelFrame(self.root, text="Resultados")
    results_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Configurar la tabla Treeview
    self.results_tree = ttk.Treeview(results_frame, columns=("Score", "Titulo", "Enlace"), show="headings")
    self.results_tree.heading("Score", text="Score")
    self.results_tree.heading("Titulo", text="Título")
    self.results_tree.heading("Enlace", text="Enlace")

    # Ajustar el ancho de las columnas
    self.results_tree.column("Score", width=80, anchor="center")
    self.results_tree.column("Titulo", width=400, anchor="w")
    self.results_tree.column("Enlace", width=300, anchor="w")

    self.results_tree.bind("<Double-1>", self.on_item_double_click) 

    self.results_tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.results_tree.yview)
    self.results_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    # Exportar
    export_frame = ttk.Frame(main_frame)
    export_frame.pack(fill="x")
    ttk.Button(export_frame, text="Guardar JSON", command=self.export_json).pack(side="left", padx=5)
    ttk.Button(export_frame, text="Guardar CSV", command=self.export_csv).pack(side="left", padx=5)
  
  def on_item_double_click(self, event):
    item_id = self.results_tree.selection() # Obtiene el ID del elemento seleccionado
    if not item_id:
      return

    # Obtiene los valores de la fila seleccionada
    item_values = self.results_tree.item(item_id, 'values')
    
    # El enlace está en la tercera columna (índice 2)
    if len(item_values) > 2:
      url = item_values[2]
      try:
        webbrowser.open_new(url) # Abre la URL en el navegador predeterminado
      except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el enlace:\n{url}\nError: {e}")

  def scrape_news(self):
    query = self.scrape_query.get().strip()
    if not query:
      messagebox.showwarning("Error", "Ingresa un tema para scrapear")
      return
    
    # Verificar caché
    cached_data = load_cache(query)
    if cached_data:
      if messagebox.askyesno("Caché encontrada", f"¿Usar datos guardados para '{query}'?"):
        self.articles = cached_data
        self.model, self.doc_vecs = train_model(self.articles)
        messagebox.showinfo("Éxito", f"Se cargaron {len(self.articles)} noticias desde caché")
        return
    
    try:
      self.root.config(cursor="watch")
      self.root.update()
      
      # Scrapear si no hay caché o el usuario quiere actualizar
      links = get_all_news(query, 10)
      self.articles = fetch_articles_content(links)
      save_cache(query, self.articles)
      self.model, self.doc_vecs = train_model(self.articles)
      
      messagebox.showinfo("Éxito", f"Se obtuvieron {len(self.articles)} noticias sobre '{query}'")
    
    except Exception as e:
      messagebox.showerror("Error", f"Error al scrapear:\n{str(e)}")
    finally:
      self.root.config(cursor="")

  def semantic_search(self):
    if not self.articles:
      messagebox.showwarning("Error", "Primero obtén noticias (Fase 1)")
      return
    
    query = self.search_query.get().strip()
    print(query)
    if not query:
      messagebox.showwarning("Error", "Ingresa una consulta")
      return
    
    try:
      scores = search(query, self.model, self.doc_vecs)
      self.show_results(scores)
    except Exception as e:
      messagebox.showerror("Error", f"Error en búsqueda:\n{str(e)}")

  def show_results(self, scores):
    self.results_tree.delete(*self.results_tree.get_children())
    
    # Ordenar artículos por score
    scored_articles = sorted(
      zip(scores, self.articles),
      key=lambda x: x[0],
      reverse=True
    )
    
    for score, article in scored_articles:
      self.results_tree.insert("", "end", values=(
        f"{score:.4f}",
        article['titulo'],
        article['enlace']
      ))
    
  def export_json(self):
    self._export_data('json')
  
  def export_csv(self):
    self._export_data('csv')
  
  def _export_data(self, format):
    if not self.articles:
      messagebox.showwarning("Error", "No hay datos para exportar")
      return
        
    file_path = filedialog.asksaveasfilename(
      defaultextension=f".{format}",
      filetypes=[(f"{format.upper()} files", f"*.{format}")]
    )
    
    if file_path:
      try:
        if format == 'json':
          with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.articles, f, ensure_ascii=False, indent=2)
        else:
          pd.DataFrame(self.articles).to_csv(file_path, index=False)
        
        messagebox.showinfo("Éxito", f"Datos exportados a {format.upper()}")
      except Exception as e:
        messagebox.showerror("Error", f"Error al exportar:\n{str(e)}")
