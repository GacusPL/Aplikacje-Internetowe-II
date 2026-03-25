import datetime
import json
import os
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class ElementCV:
    next_id = 1
    
    @classmethod
    def zainicjalizuj_id(cls, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if data:
                        cls.next_id = max((item.get('id', 0) for item in data), default=0) + 1
                except (json.JSONDecodeError, ValueError):
                    pass
    
    @classmethod
    def pobierz_kolejne_id(cls):
        aktualne_id = cls.next_id
        cls.next_id += 1
        return aktualne_id

ElementCV.zainicjalizuj_id('cv_database.json')

@app.route("/", methods=['GET'])
def index():
    return "/generator"

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    if request.method == 'POST':
        email = request.form.get('email', '')
        
        if '@' not in email:
            app.logger.error("Błąd walidacji: Email nie zawiera znaku '@'")
            return "Błąd: Email musi zawierać znak '@'", 400

        nowe_cv = {
            "id": ElementCV.pobierz_kolejne_id(),
            "fullname": request.form.get('fullname'),
            "email": email,
            "github": request.form.get('github'),
            "position": request.form.get('position'),
            "skills": request.form.get('skills', '').split(','),
            "experience": request.form.get('experience')
        }

        file_path = 'cv_database.json'
        data = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        # Zabezpieczenie przed podwójnym zapisem przy odświeżeniu
        is_duplicate = False
        if data:
            ostatnie_cv = data[-1]
            if (ostatnie_cv.get('email') == nowe_cv['email'] and 
                ostatnie_cv.get('fullname') == nowe_cv['fullname'] and 
                ostatnie_cv.get('position') == nowe_cv['position']):
                nowe_cv['id'] = ostatnie_cv.get('id')
                ElementCV.next_id -= 1

        if not is_duplicate:
            data.append(nowe_cv)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        return render_template('szablon_cv.html', cv=nowe_cv)

    return render_template('formularz_cv.html')

if __name__ == '__main__':
    app.run(debug=True)
