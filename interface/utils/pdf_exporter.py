import textwrap
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_pdf(self):
  max_link_chars = 60 

  if not self.articles:
    messagebox.showwarning("Error", "No hay datos para exportar")
    return

  # Obtiene el termino general y particular
  tema_inicial = self.scrape_query.get().strip()
  consulta = self.search_query.get().strip()

  file_path = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")]
  )
  if not file_path:
    return

  try:
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    y = height - 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "Resultados de Búsqueda Semántica")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(40, y, f"Tema inicial: {tema_inicial}")
    y -= 20
    c.drawString(40, y, f"Consulta: {consulta}")
    y -= 30

    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y, "Score")
    c.drawString(100, y, "Título")
    c.drawString(350, y, "Enlace")
    y -= 15
    c.setFont("Helvetica", 10)

    # Exporta exactamente lo que está en el Treeview
    for item in self.results_tree.get_children():
      values = self.results_tree.item(item, 'values')
      if len(values) == 3:
        score, titulo, enlace = values
        c.drawString(40, y, str(score))
        c.drawString(100, y, str(titulo)[:40])
        wrapped_link = textwrap.wrap(str(enlace), width=max_link_chars)
        for i, line in enumerate(wrapped_link):
          c.drawString(350, y - i*12, line)
        y -= max(15, 12 * len(wrapped_link))
        if y < 50:
          c.showPage()
          y = height - 40
          c.setFont("Helvetica-Bold", 10)
          c.drawString(40, y, "Score")
          c.drawString(100, y, "Título")
          c.drawString(350, y, "Enlace")
          y -= 15
          c.setFont("Helvetica", 10)

    c.save()
    messagebox.showinfo("Éxito", "Resultados exportados a PDF")
  except Exception as e:
    messagebox.showerror("Error", f"Error al exportar PDF:\n{str(e)}")
