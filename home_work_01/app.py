from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html', shoes=data.shoes)

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html', clothes=data.clothes)

@app.route('/hats/')
def hats():
    return render_template('hats.html', hats=data.hats)


if __name__ == '__main__':
    app.run(debug=True)
