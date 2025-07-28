# IFC-PARSER

Projekt zawiera dwa główne narzędzia do pracy z plikami IFC:

1. **IFC Valid Checker** — do weryfikacji poprawności plików IFC  
2. **PropertySet Parser** — do analizy i wyciągania zestawów właściwości (Property Sets) z modeli IFC

---

## IFC Valid Checker

Narzędzie służy do sprawdzania poprawności plików IFC oraz ich podstawowej analizy.

### Funkcjonalności

- Wczytywanie plików IFC i IFC ZIP przez okno dialogowe.
- Podstawowa walidacja struktury i zawartości pliku IFC.
- Wyświetlanie informacji o wybranym pliku.
- Obsługa błędów podczas otwierania i analizy pliku.

### Wymagania

- Python 3.6+
- Biblioteka [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
- Tkinter (wbudowany w Pythona)

### Uruchomienie
- W folderze INSTALATORY znajduje się link do Google drive, gdzie znajdują się pliki .exe dla obydwu programów oraz przykładowe wyniki analiz

### Uruchomienie

```bash
python ifc_valid_checker.py



