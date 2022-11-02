from flask import Flask, render_template
import utils



app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>/')
def profile(uid):
    candidate = utils.get_candidate_by_id(uid)
    if candidate is None:
        return "Нет такого кандидата"
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>/')
def search_by_candidates_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    candidates_amount = len(candidates)
    return render_template('search.html',
                           candidates=candidates,
                           candidates_amount=candidates_amount
                           )


@app.route('/skill/<skill_name>/')
def search_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    candidates_amount = len(candidates)
    return render_template('skill.html',
                           candidates=candidates,
                           candidates_amount=candidates_amount,
                           skill_name=skill_name
                           )


app.run()
