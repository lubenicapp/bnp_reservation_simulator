from flask import Flask, render_template, request
from datetime import date
import random

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
    firstnames = []
    lastnames = []
    host = ['cetelem', 'bnpparibas-pf']
    with open('names.csv') as file:
        for line in file:
            split = line.replace(',', ' ').split(' ')
            firstnames.append(split[0])
            lastnames.append(split[1])

    email = f'{random.choice(firstnames)}.{random.choice(lastnames)}@{random.choice(host)}.com'
    return email

    pass

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
    app.run()

