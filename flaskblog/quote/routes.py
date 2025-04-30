from flask import render_template, Blueprint, url_for, redirect, flash
from flask_login import login_required, current_user, login_user
import random

quote = Blueprint('quote', __name__)

@login_required
@quote.route("/quote", methods=['GET'])
def check_quote_of_the_day():
    if current_user.is_authenticated:
        num = random.randrange(0, 3)
        quotes = {0 : "Quote 1", 1 : "Quote 2", 2 : "Quote 3"}
        quote = quotes[num]
        return render_template('quote.html', title='Quote', quote=quote)
    else:
        flash("You need to login in first to see quote!", "info")
        return redirect(url_for('main.home'))
