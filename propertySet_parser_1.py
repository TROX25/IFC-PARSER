# import biblioteki do ifc
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from tkinter import Tk, filedialog, messagebox

# Ukrycie okna GUI - niepotrzebne 
root = Tk()
root.withdraw()

# wybór pliku
file_path = filedialog.askopenfilename(
        title = "Wybierz plik",
        filetypes=[("IFC files", "*.ifc"), ("IFC ZIP files", "*.ifczip"), ("All files", "*.*")]
    )

# przypisanie do zmiennej ifc wybranego pliku    
ifc = ifcopenshell.open(file_path)

# możliwości parsa
schema = ifc.schema # pokazuje wersję IFC
first_line = ifc.by_id(1) # pokazuje pierwszą linijkę
software_name = first_line.Name 

# Info dla usera
messagebox.showinfo("Informacja", "Wybierz miejsce zapisu wyników analizy.")

# Wybór miejsca zapisu
save_path = filedialog.asksaveasfilename(
    title="Zapisz wyniki jako",
    defaultextension=".txt",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

# Wybór informacji do eksportu
with open(save_path, "w", encoding="utf-8") as plik:
        plik.write(f"Wersja IFC: {schema}\n")
        plik.write(f"Pierwszy Obiekt: {str(first_line)}\n")
        plik.write(f"Wersja Revit: {software_name[:-5]}\n")  # usuwam ostatnie 5 znaków (ENU)??



# Parse p-setów (Pset -> properties -> )

# if __name__ == "main":
#   XXXX