from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/searchpage')
def searchpage():
    return render_template('searchpage.html')

@app.route('/recipepage/<idVal>')
def recipepage(idVal):
    return render_template('recipepage.html', id=idVal)

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/ingredientsearch')
def ingredientsearch():
    return render_template('ingredientsearch.html')

@app.route('/countrylist/<countryVal>')
def countrylist(countryVal):
    return render_template('countrylist.html', country=countryVal)

@app.route('/categorylist/<categoryVal>')
def categorylist(categoryVal):
    return render_template('categorylist.html', category=categoryVal)


if __name__ == "__main__":
    app.run(port=5000, debug=True)