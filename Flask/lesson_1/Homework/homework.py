from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route('/')
def page_main():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candidates += '</pre>'
    return str_candidates


@app.route('/candidates/<int:id>')
def profile(id):
    candidate = candidates[id]
    str_candidates = f"{candidate['name']} <br><br>{candidate['position']} <br>{candidate['skills']} <br><br>"
    return str_candidates


@app.route('/skills/<skill>')
def profile_skill(skill):
    str_candidates = '<pre>'
    skill_lower = skill.lower()
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(", ")
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill_lower in candidate_skills:
            str_candidates += f"{candidate['name']} <br><br>{candidate['position']} <br>{candidate['skills']} <br><br>"

    str_candidates += '<pre>'

    return str_candidates


app.run()


"""нужно поменять репозитории который был изначально здесь на новый, минута 50 видео"""

