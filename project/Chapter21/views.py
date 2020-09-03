from flask import Blueprint, render_template

chap21 = Blueprint("chap21", __name__)

@chap21.route('/trans_timing_func')
def trans_timing_func():
    return render_template('chapter21/transition_timing_functions.html')