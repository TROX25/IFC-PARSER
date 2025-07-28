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

---

## PropertySet Parser

Narzędzie do parsowania i analizy zestawów właściwości (Property Sets) w plikach IFC.

### Funkcjonalności

- Wczytywanie plików IFC przez GUI.
- Parsowanie PSetów, np. `Pset_SiteCommon`, `Pset_BuildingElementProxyCommon`.
- Filtrowanie i eksport wybranych danych do pliku tekstowego.
- Obsługa plików `.ifc` oraz `.ifczip`.

---

## Pliki i przykłady

- W folderze `INSTALATORY` znajduje się link do Google Drive z plikami `.exe` dla obu programów.
- W folderze `IFC Examples` znajdują się przykładowe pliki IFC wraz z wynikami analiz.

---

## Instrukcja obsługi (dla obu programów)

### 1. Uruchomienie pliku `.exe`

- Otwórz folder `INSTALATORY` i uruchom odpowiedni plik `.exe` (np. `ifc_valid_checker.exe` lub `propertyset_parser.exe`).

<img width="265" height="57" alt="Zrzut ekranu 2025-07-28 030322" src="https://github.com/user-attachments/assets/7c254fc3-9196-448c-9e39-607ffa8bc38c" />
*Przykładowy widok uruchomionego pliku exe.*

---

### 2. Wybór pliku IFC do analizy

- Po uruchomieniu pojawi się okno dialogowe.
- Wybierz plik IFC (`.ifc` lub `.ifczip`) do analizy.

![Wybór pliku IFC](./docs/images/step2_select_ifc.png)  
*Okno wyboru pliku IFC.*

---

### 3. Wybór miejsca zapisu pliku `.txt`

- Po zakończeniu analizy program poprosi o wskazanie miejsca i nazwy pliku `.txt`, gdzie zostanie zapisany wynik analizy.

![Wybór miejsca zapisu](./docs/images/step3_save_txt.png)  
*Okno wyboru lokalizacji zapisu wyników.*

---

### 4. Rezultat

- Po zapisaniu pliku tekstowego, znajdziesz tam szczegółowe dane z analizy.
- Przykładowy wynik może zawierać listę Property Sets, błędy walidacji lub inne wybrane informacje.

![Przykładowy rezultat](./docs/images/step4_result.png)  
*Przykład wygenerowanego pliku tekstowego z analizą.*

---

## Instalacja (wersja dla Pythona)

Jeśli chcesz uruchomić programy z kodu źródłowego:

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/TROX25/IFC-PARSER.git
   cd IFC-PARSER
