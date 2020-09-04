from flask import Blueprint, render_template

chap43 = Blueprint('chap43', __name__)

@chap43.route('/flexnavbar')
def flexnavbar():
    return render_template('chapter43/flexnavbar.html')