from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_required, current_user, login_user
import random

quote = Blueprint('quote', __name__)

@login_required
@quote.route("/quote", methods=['GET', 'POST'])
def check_quote_of_the_day():

    if request.method == "GET":
        return render_template("quote.html", files_list=[6], sides_default=6, dice_default=1)
    if request.method == "POST":

        if current_user.is_authenticated:
            num_sides = int(request.form.get("num_sides"))
            num_dice = int(request.form.get("num_dice"))

            chosen_nums = []
            for x in range(0, num_dice):
                chosen_nums.append(random.randint(1, num_sides))
            
            files_list = []
            for item in chosen_nums:
                files_list.append(item)
            total = sum(files_list) % 6
            quotes = {0 : "Quote 1", 1 : "Quote 2", 2 : "Quote 3", 3 : "Quote 4", 4 : "Quote 5", 5 : "Quote 6"}
            chosen_quote = quotes[total]

            
            return render_template('quote.html', title='Quote', files_list=files_list, sides_default=num_sides, dice_default=num_dice, chosen_quote=chosen_quote)
        else:
            flash("You need to login in first to see quote!", "info")
            return redirect(url_for('main.home'))
