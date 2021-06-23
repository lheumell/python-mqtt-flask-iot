from flask import Flask, render_template
import methods

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pyecharts.html', instant=methods.temperaturesInstant(), rows=methods.temperaturesValue())

@app.route('/list')
def list():
    return render_template("list.html", rows=methods.temperatures())


if __name__ == '__main__':
    app.run(debug=True)
