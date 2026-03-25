import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Wiadomosc:
    def __init__(self, imie_uzytkownika, tresc):
        self.imie_uzytkownika = imie_uzytkownika
        self.tresc = tresc
        
    def drukuj(self):
        print(f"Obiekt Wiadomosc - Imię: {self.imie_uzytkownika}, Wiadomość: {self.tresc}")

@app.route("/", methods=['GET'])
def index():
    return "/kontakt"

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == 'POST':
        #Zad 2
        imie = request.form.get('imie_uzytkownika')
        wiadomosc = request.form.get('tresc')
        
        #Zad 3
        obiekt_wiadomosc = Wiadomosc(imie, wiadomosc)
        obiekt_wiadomosc.drukuj()
        app.logger.info(f"Utworzono obiekt Wiadomosc dla: {imie}")
        
        #Zad 4
        dane = {
            "imie": imie,
            "wiadomosc": wiadomosc,
            "status": "odebrano",
            "liczba_znakow": len(wiadomosc) if wiadomosc else 0,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        app.logger.info(f"Wygenerowano odpowiedź JSON dla: {imie}")
        
        return jsonify(dane)
        
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)
