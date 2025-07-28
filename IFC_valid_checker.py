import ifcopenshell
from tkinter import Tk, filedialog, messagebox


def main():
    root = Tk()
    root.withdraw()

    # Wybór pliku IFC
    file_path = filedialog.askopenfilename(
        title="Wybierz plik IFC",
        filetypes=[("IFC files", "*.ifc"), ("IFC ZIP files", "*.ifczip"), ("All files", "*.*")]
    )
    if not file_path:
        messagebox.showinfo("Anulowano", "Nie wybrano pliku.")
        return

    try:
        ifc = ifcopenshell.open(file_path)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się otworzyć pliku IFC.\n{e}")
        return

    results = []

    ifc_project = ifc.by_type("IfcProject")
    if ifc_project:
        results.append("Element IfcProject: obecny")
    else:
        results.append("Brak elementu IfcProject - plik prawdopodobnie nie jest kompletny.")

    ifc_site = ifc.by_type("IfcSite")
    if ifc_site:
        results.append("Element IfcSite: obecny")
    else:
        results.append("Brak elementu IfcSite - plik prawdopodobnie nie jest kompletny.")
        
    if ifc_site and ifc_project:
        results.append("Plik ifc jest kompletny")
        

    # Informacja dla użytkownika o zapisie
    messagebox.showinfo("Informacja", "Wybierz miejsce zapisu wyników analizy.")

    # Wybór miejsca zapisu pliku tekstowego
    save_path = filedialog.asksaveasfilename(
        title="Zapisz wyniki jako",
        defaultextension=".txt",
        filetypes=[("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")]
    )


    # Zapis wyników do pliku
    with open(save_path, "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")



if __name__ == "__main__":
    main()
