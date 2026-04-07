import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'praktyki-secret-key'

# ── Pliki bazy danych ──────────────────────────────────────────────────────────
ZAL4_FILE = 'zal4_database.json'
ZAL6_FILE = 'zal6_database.json'


# ── Logika bazy danych (wzorowana na zadaniu wprowadzającym) ───────────────────

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def find_student(records, nr_albumu):
    """Zwraca rekord studenta lub None."""
    for r in records:
        if r.get('nr_albumu') == nr_albumu:
            return r
    return None


# ── Efekty uczenia się (Załącznik nr 4) ───────────────────────────────────────

EFEKTY = [
    {'id': '01', 'opis': 'Ma wiedzę na temat sposobu realizacji zadań inżynierskich dotyczących informatyki z zachowaniem standardów i norm technicznych'},
    {'id': '02', 'opis': 'Zna technologie, narzędzia, metody, techniki oraz sprzęt stosowane w informatyce'},
    {'id': '03', 'opis': 'Zna ekonomiczne, prawne skutki własnych działań podejmowanych w ramach praktyki oraz ograniczenia wynikające z prawa autorskiego i kodeksu pracy'},
    {'id': '04', 'opis': 'Zna zasady bezpieczeństwa pracy i ergonomii w zawodzie informatyka'},
    {'id': '05', 'opis': 'Pozyskuje informacje odnośnie technologii, metod, technik, sprzętu wymaganego do realizacji powierzonego zadania, posługując się rozmaitymi źródłami literaturowymi i zasobami publikowanymi w języku polskim jak i angielskim'},
    {'id': '06', 'opis': 'W oparciu o kontakty ze środowiskiem inżynierskim zakładu, potrafi podnieść swoje kompetencje, wiedzę i umiejętności, co najmniej z dwóch zakresów: zadania dotyczące sprzętu i oprogramowania'},
    {'id': '07', 'opis': 'Opracowuje dokumentację dotyczącą realizacji podejmowanych zadań w ramach praktyki, a także referuje ustnie prezentowane w niej zagadnienia'},
    {'id': '08', 'opis': 'Potrafi zidentyfikować problem informatyczny występujący w zakładzie pracy/instytucji, opisać go, przedstawić koncepcję rozwiązania i ją zrealizować'},
    {'id': '09', 'opis': 'Potrafi rozwiązać rzeczywiste zadanie inżynierskie z zakresu działalności informatycznej zakładu pracy/instytucji stosując normy i standardy oraz biorąc pod uwagę aspekty środowiskowe i etyczne'},
    {'id': '10', 'opis': 'Pracuje w zespole zajmującym się zawodowo branżą IT'},
    {'id': '11', 'opis': 'Przestrzega zasad etyki zawodowej i zgodnie z tymi zasadami korzysta z wiedzy i pomocy doświadczonych kolegów'},
    {'id': '12', 'opis': 'Kontaktując się z osobami spoza branży potrafi zarówno pozyskać od nich niezbędne informacje do realizacji planowanego zadania, jak i przekazać im w sposób zrozumiały informacje i opinie z zakresu informatyki'},
    {'id': '13', 'opis': 'Dostrzega w praktyce tempo deaktualizacji wiedzy informatycznej oraz skutki działalności informatyków, w szczególności ekonomiczne i społeczne'},
]


# ── Strona główna ──────────────────────────────────────────────────────────────

@app.route('/')
def index():
    studenci_zal4 = load_data(ZAL4_FILE)
    studenci_zal6 = load_data(ZAL6_FILE)
    return render_template('index.html',
                           liczba_zal4=len(studenci_zal4),
                           liczba_zal6=len(studenci_zal6))


# ── Załącznik 4 - lista studentów ─────────────────────────────────────────────

@app.route('/zal4')
def zal4_lista():
    studenci = load_data(ZAL4_FILE)
    return render_template('zal4_lista.html', studenci=studenci)


# ── Załącznik 4 – nowy / edycja ───────────────────────────────────────────────

@app.route('/zal4/nowy')
def zal4_nowy():
    return render_template('zal4_formularz.html', student=None, efekty=EFEKTY)


@app.route('/zal4/edytuj/<nr_albumu>')
def zal4_edytuj(nr_albumu):
    studenci = load_data(ZAL4_FILE)
    student = find_student(studenci, nr_albumu)
    if not student:
        flash('Nie znaleziono studenta.', 'error')
        return redirect(url_for('zal4_lista'))
    return render_template('zal4_formularz.html', student=student, efekty=EFEKTY)


@app.route('/zal4/zapisz', methods=['POST'])
def zal4_zapisz():
    studenci = load_data(ZAL4_FILE)
    nr_albumu = request.form.get('nr_albumu', '').strip()

    # Zbierz wyniki dla każdego efektu
    wyniki_efektow = {}
    for e in EFEKTY:
        wyniki_efektow[e['id']] = request.form.get(f'efekt_{e["id"]}', 'nie uzyskal')

    nowy_rekord = {
        'nr_albumu':    nr_albumu,
        'imie_nazwisko': request.form.get('imie_nazwisko', '').strip(),
        'specialnosc':  request.form.get('specialnosc', '').strip(),
        'liczba_godzin': request.form.get('liczba_godzin', '').strip(),
        'wynik_ogolny': request.form.get('wynik_ogolny', 'nie uzyskal'),
        'wyniki_efektow': wyniki_efektow,
        'opinia_opiekuna': request.form.get('opinia_opiekuna', '').strip(),
    }

    # Aktualizuj istniejący lub dodaj nowy
    istniejacy = find_student(studenci, nr_albumu)
    if istniejacy:
        idx = studenci.index(istniejacy)
        studenci[idx] = nowy_rekord
        flash('Dane studenta zaktualizowane.', 'success')
    else:
        studenci.append(nowy_rekord)
        flash('Dodano nowego studenta.', 'success')

    save_data(studenci, ZAL4_FILE)
    return redirect(url_for('zal4_lista'))


@app.route('/zal4/usun/<nr_albumu>', methods=['POST'])
def zal4_usun(nr_albumu):
    studenci = load_data(ZAL4_FILE)
    studenci = [s for s in studenci if s.get('nr_albumu') != nr_albumu]
    save_data(studenci, ZAL4_FILE)
    flash('Rekord usunięty.', 'success')
    return redirect(url_for('zal4_lista'))


# ── Załącznik 6 – lista studentów ─────────────────────────────────────────────

@app.route('/zal6')
def zal6_lista():
    studenci = load_data(ZAL6_FILE)
    return render_template('zal6_lista.html', studenci=studenci)


# ── Załącznik 6 – nowy / edycja ───────────────────────────────────────────────

@app.route('/zal6/nowy')
def zal6_nowy():
    return render_template('zal6_formularz.html', student=None)


@app.route('/zal6/edytuj/<nr_albumu>')
def zal6_edytuj(nr_albumu):
    studenci = load_data(ZAL6_FILE)
    student = find_student(studenci, nr_albumu)
    if not student:
        flash('Nie znaleziono studenta.', 'error')
        return redirect(url_for('zal6_lista'))
    return render_template('zal6_formularz.html', student=student)


@app.route('/zal6/zapisz', methods=['POST'])
def zal6_zapisz():
    studenci = load_data(ZAL6_FILE)
    nr_albumu = request.form.get('nr_albumu', '').strip()

    # Pobierz listowe dane tabeli dziennika (wzorowane na zadaniu 4 z lab)
    dni        = request.form.getlist('dzien[]')
    daty       = request.form.getlist('data[]')
    opisy      = request.form.getlist('opis[]')
    nr_efektow = request.form.getlist('nr_efektow[]')

    wpisy = [
        {
            'dzien':      d,
            'data':       da,
            'opis':       op,
            'nr_efektow': ne,
        }
        for d, da, op, ne in zip(dni, daty, opisy, nr_efektow)
        if op.strip()   # pomijaj puste wiersze
    ]

    nowy_rekord = {
        'nr_albumu':          nr_albumu,
        'imie_nazwisko':      request.form.get('imie_nazwisko', '').strip(),
        'zakres':             request.form.get('zakres', '').strip(),
        'rok_akademicki':     request.form.get('rok_akademicki', '').strip(),
        'miejsce_praktyki':   request.form.get('miejsce_praktyki', '').strip(),
        'data_rozpoczecia':   request.form.get('data_rozpoczecia', '').strip(),
        'data_zakonczenia':   request.form.get('data_zakonczenia', '').strip(),
        'wykaz_zalacznikow':  request.form.get('wykaz_zalacznikow', '').strip(),
        'wpisy':              wpisy,
    }

    istniejacy = find_student(studenci, nr_albumu)
    if istniejacy:
        idx = studenci.index(istniejacy)
        studenci[idx] = nowy_rekord
        flash('Dziennik zaktualizowany.', 'success')
    else:
        studenci.append(nowy_rekord)
        flash('Dodano nowy dziennik.', 'success')

    save_data(studenci, ZAL6_FILE)
    return redirect(url_for('zal6_lista'))


@app.route('/zal6/usun/<nr_albumu>', methods=['POST'])
def zal6_usun(nr_albumu):
    studenci = load_data(ZAL6_FILE)
    studenci = [s for s in studenci if s.get('nr_albumu') != nr_albumu]
    save_data(studenci, ZAL6_FILE)
    flash('Rekord usunięty.', 'success')
    return redirect(url_for('zal6_lista'))


if __name__ == '__main__':
    app.run(debug=True)
