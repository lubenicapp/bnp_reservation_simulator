from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
          'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']



@app.route('/')
def landing():

    hours = []
    for i in range(11, 14, 1):
        for j in range(0, 60, 10):
            hours.append(f"{i}:{j:02d}")
    hours = hours[3::]

    today = date.today()
    day = today.strftime('%d')
    month = months[int(today.strftime('%m')) - 1]
    year = today.strftime('%Y')
    now = f'{day} {month} {year}'

    return render_template('index.html', now=now, hours=hours)


@app.route('/reservation')
def reservation():

    date = request.args['date']
    hour = request.args['hour']
    email = request.args['email']

    return render_template('reservation.html', date=date, hour=hour, email=email)


if __name__ == '__main__':
    app.run()

