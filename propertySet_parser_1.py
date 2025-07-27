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

    # możliwości parsa
    schema = ifc.schema # type: ignore # pokazuje wersję IFC
    first_line = ifc.by_id(1) # type: ignore # pokazuje pierwszą linijkę
    software_name = first_line.Name # type: ignore # pokazuje wersje revita
    psets = ifc.by_type("IfcPropertySet")   # type: ignore # wybiera wszystkie property sety
    properties = ifc.by_type("IfcProperty") # type: ignore # wybiera wszystkie parametry 

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
            #plik.write(f"Pierwszy Obiekt: {str(first_line)}\n")
            plik.write(f"Wersja Revit: {software_name[:-5]}\n\n")  # usuwam ostatnie 5 znaków (ENU)??
            
            # Set (bez duplikatów) dla Psetów
            psety_noDupes = set()
            
            # Wyszukuje Psety [ALE TYLKO TE ZACZYNAJĄCE SIE OD Pset - czyli nie wszystkie (bez np. BaseQuantities, Dimensions, Reference)]
            plik.write("Wszyskie Psety:\n")
            for pset in psets:
                if pset.Name.startswith("Pset"):
                    if pset.Name not in psety_noDupes:
                        psety_noDupes.add(pset.Name)
                        plik.write(f"{pset.Name}\n")
                        
                        if hasattr(pset, "HasProperties") and pset.HasProperties:
                            for property in pset.HasProperties:
                                property_name = property.Name
                                if hasattr(property, "NominalValue") and property.NominalValue:
                                    content = property.NominalValue.wrappedValue
                                    plik.write(f"   - {property_name}: {content}\n")
                                else:
                                    plik.write(f"   - {property_name}: -\n")
                        else:
                            plik.write("Brak Danych !!!\n")
                    
            # z Seta psety_noDupes dodaje alfabetycznie do pliku txt  
            
            ## NIE MUSI BYĆ PO KOLEI ALE MOŻE ##      
            #for xxx in sorted(psety_noDupes):
            #    plik.write(f"{xxx}\n")
                
                
                        

                    


# Parse p-setów (Pset -> properties -> )

if __name__ == "__main__":
    main()