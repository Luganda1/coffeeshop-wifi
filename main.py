from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="This Field is required")])
    location = StringField('Location',
                           validators=[DataRequired(message="This Field is required"),
                                       URL(require_tld=True, message="e.g.https://getbootstrap.com/")])
    open = StringField('Open', validators=[DataRequired(message="This Field is required")])
    close = StringField('Close', validators=[DataRequired(message="This Field is required")])
    coffee = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField("Wifi Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField("Power Socket ", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        openi = form.open.data
        close = form.close.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        with open('cafe-data.csv', 'a', newline='', encoding="utf-8") as df:
            df.write(f"\n{cafe}, {location}, {openi}, {close}, {coffee}, {wifi}, {power}")
        return redirect(url_for('cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        first_line = True
        for row in csv_data:
            if not first_line:
                list_of_rows.append({
                    "Cafe name": row[0],
                    "Location": row[1],
                    "Open": row[2],
                    "Close": row[3],
                    "Coffee": row[4],
                    "Wifi": row[5],
                    "Power": row[6],
                })
            else:
                first_line = False
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
