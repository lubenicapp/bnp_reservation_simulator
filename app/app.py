from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('templates/index.html')

@app.route('/reservation')
def reservation():

    date = request.args['date']
    hour = request.args['hour']
    email = request.args['email']

    return render_template('templates/reservation.html', date=date, hour=hour, email=email)


if __name__ == '__main__':
    app.run()

