# import biblioteki do ifc
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from tkinter import Tk, filedialog, messagebox


def main():
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

if __name__ == "__main__":
    main()