from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flaskapp <=> routing"


@app.route('/simple-interest', methods=['GET', 'POST'])
def simple_interest():

    if request.method == 'POST':
        p = float(request.form['principal'])
        r = float(request.form['rate'])
        t = float(request.form['time'])

        si = (p * r * t) / 100
        amount = p + si

        return render_template(
            'simple_interest.html',
            si=si,
            amount=amount
        )

    return render_template('index.html')


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"


if __name__ == '__main__':
    app.run(debug=True, port=3500)