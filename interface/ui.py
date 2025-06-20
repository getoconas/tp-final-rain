from tkinter import ttk, messagebox, filedialog

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
  ttk.Button(export_frame, text="Exportar PDF", command=self.export_pdf).pack(side="left", padx=5)
