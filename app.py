from flask import Flask, render_template, request
from datetime import date
import random
from firstnames import firstnames
from lastnames import lastnames

app = Flask(__name__)

months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
          'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']


def get_hours():
    hours = []
    for i in range(11, 14, 1):
        for j in range(0, 60, 10):
            hours.append(f"{i}:{j:02d}")
    hours = hours[3::]
    return hours


def random_email():
    host = ['cetelem', 'bnpparibas-pf']
    email = f'{random.choice(firstnames)}.{random.choice(lastnames)}@{random.choice(host)}.com'
    return email.lower()


def get_today():
    today = date.today()
    day = today.strftime('%d')
    month = months[int(today.strftime('%m')) - 1]
    year = today.strftime('%Y')
    now = f'{day} {month} {year}'
    return now

@app.route('/')
def landing():
    return render_template('index.html', email=random_email(), now=get_today(), hours=get_hours())


@app.route('/reservation')
def reservation():
    date = request.args['date']
    hour = request.args['hour']
    email = request.args['email']
    return render_template('reservation.html', date=date, hour=hour, email=email)


if __name__ == '__main__':
    load_email()
    app.run()

