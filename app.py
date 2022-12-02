from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route('/')
def get_list():
    candidates = utils.get_all_candidate()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def get_candidate(candidate_id):
    candidate = utils.get_candidate_by_id(candidate_id)
    return render_template('card.html', candidate=candidate[0])


@app.route('/search/<candidate_name>')
def get_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, num_candidates=len(candidates))


@app.route('/skill/<skill_name>')
def get_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name)


if __name__ == "__main__":
    app.run()
