from flask import flask, render_template, redirect, url_for

app = flask(__name__)

@app.route('/')
def index():
    return render_template('first_page.html')

@app.route('/second_page')
def second_page():
    return render_template('second_page.html')

@app.route('/back_to_first_page')
def back_to_first_page():
    return redirect(url_for('index'))

@app.route('/try',method=['GET'])
def fun():
    return 'Working Successfully!!'

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')