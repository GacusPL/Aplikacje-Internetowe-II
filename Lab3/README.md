# System Rozliczenia Praktyk Zawodowych

Aplikacja Flask do obsługi formularzy związanych z rozliczeniem praktyk
(Akademia Nauk Stosowanych w Elblągu – Instytut Informatyki Stosowanej).

## Struktura projektu

```
praktyki_app/
├── app.py                  # Główna logika Flask (trasy, baza danych)
├── requirements.txt
├── zal4_database.json      # Baza danych – Załącznik nr 4 (tworzony automatycznie)
├── zal6_database.json      # Baza danych – Załącznik nr 6 (tworzony automatycznie)
├── static/
│   └── style.css
└── templates/
    ├── base.html           # Szablon bazowy (navbar, flash messages)
    ├── index.html          # Strona główna
    ├── zal4_lista.html     # Lista studentów – Zał. 4
    ├── zal4_formularz.html # Formularz Zał. 4 (nowy / edycja)
    ├── zal6_lista.html     # Lista studentów – Zał. 6
    └── zal6_formularz.html # Formularz Zał. 6 z dynamiczną tabelą JS
```

## Uruchomienie

```bash
pip install -r requirements.txt
python app.py
# Otwórz http://127.0.0.1:5000
```

## Dane (JSON)

### zal4_database.json
```json
[
  {
    "nr_albumu": "12345",
    "imie_nazwisko": "Jan Kowalski",
    "specialnosc": "Systemy informatyczne",
    "liczba_godzin": "120",
    "wynik_ogolny": "uzyskal",
    "wyniki_efektow": {
      "01": "uzyskal",
      "02": "uzyskal",
      ...
    },
    "opinia_opiekuna": "Student wykazał się..."
  }
]
```

### zal6_database.json
```json
[
  {
    "nr_albumu": "12345",
    "imie_nazwisko": "Jan Kowalski",
    "zakres": "programowanie, administracja siecią",
    "rok_akademicki": "2024/2025",
    "miejsce_praktyki": "Firma XYZ Sp. z o.o.",
    "data_rozpoczecia": "2025-07-01",
    "data_zakonczenia": "2025-09-30",
    "wykaz_zalacznikow": "",
    "wpisy": [
      {
        "dzien": "1",
        "data": "2025-07-01",
        "opis": "Zapoznanie z infrastrukturą firmy...",
        "nr_efektow": "04, 05"
      }
    ]
  }
]
```

## Kluczowe wzorce (z laboratorium)

- **load_data / save_data** – zapis/odczyt JSON (Zadanie 1 z lab)
- **Pętla Jinja2** – generowanie wierszy tabel z `{% for %}` (Zadanie 2 z lab)
- **addRow / addAfter / deleteRow** – manipulacja DOM w czystym JS (Zadanie 3 z lab)
- **request.form.getlist('pole[]')** – odbiór listowych danych tabeli (Zadanie 4 z lab)
