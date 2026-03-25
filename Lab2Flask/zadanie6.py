import datetime
import json
import os
import logging
from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

class Kandydat:
    def __init__(self, fullname, email, github, position, skills_str, experience):
        self.fullname = fullname
        self.email = email
        self.github = github
        self.position = position
        
        skills_clean = [s.strip().upper() for s in skills_str.split(',') if s.strip()]
        self.skills = sorted(skills_clean)
        self.experience = experience

    def get_experience_level(self):
        length = len(self.experience)
        if length < 50:
            return "Junior"
        elif length <= 150:
            return "Mid"
        else:
            return "Senior"

    def to_dict(self):
        return {
            "fullname": self.fullname,
            "email": self.email,
            "github": self.github,
            "position": self.position,
            "skills": self.skills,
            "experience": self.experience,
            "experience_level": self.get_experience_level()
        }

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
        fullname = request.form.get('fullname', '').strip()
        email = request.form.get('email', '').strip()
        github = request.form.get('github', '').strip()
        position = request.form.get('position', '').strip()
        skills_str = request.form.get('skills', '')
        experience = request.form.get('experience', '').strip()

        errors = []
        if len(fullname.split()) < 2:
            errors.append("Pole fullname musi zawierać co najmniej dwa wyrazy (imię i nazwisko).")
        if not github.startswith("https://github.com/"):
            errors.append("Link do GitHub musi zaczynać się od 'https://github.com/'.")
        if '@' not in email:
            errors.append("Adres email musi zawierać znak '@'.")

        if errors:
            return render_template('formularz_cv.html', errors=errors)

        kandydat = Kandydat(fullname, email, github, position, skills_str, experience)
        kand_dict = kandydat.to_dict()

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
        for i, item in enumerate(data):
            if item.get('email') == kand_dict['email']:
                kand_dict['id'] = item.get('id')
                data[i] = kand_dict
                is_duplicate = True
                break

        if not is_duplicate:
            kand_dict['id'] = ElementCV.pobierz_kolejne_id()
            data.append(kand_dict)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return render_template('szablon_cv.html', cv=kand_dict)

    return render_template('formularz_cv.html')

@app.route('/admin/cv', methods=['GET'])
def admin_cv():
    file_path = 'cv_database.json'
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    return render_template('szablon_admin.html', cv_list=data)

@app.route('/download_cv/<int:cv_id>', methods=['GET'])
def download_cv(cv_id):
    file_path = 'cv_database.json'
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    
    cv_data = next((item for item in data if item.get('id') == cv_id), None)
    if not cv_data:
        return "CV not found", 404

    text_content = f"Imię i nazwisko: {cv_data.get('fullname')}\n"
    text_content += f"Stanowisko: {cv_data.get('position')}\n"
    text_content += f"Email: {cv_data.get('email')}\n"
    text_content += f"GitHub: {cv_data.get('github')}\n\n"
    text_content += "Umiejętności:\n"
    for skill in cv_data.get('skills', []):
        text_content += f"- {skill}\n"
    text_content += f"\nDoświadczenie ({cv_data.get('experience_level', 'Brak')}):\n{cv_data.get('experience')}\n"

    response = make_response(text_content)
    response.headers["Content-Disposition"] = f"attachment; filename=cv_{cv_id}.txt"
    response.headers["Content-type"] = "text/plain; charset=utf-8"
    return response

if __name__ == '__main__':
    app.run(debug=True)
