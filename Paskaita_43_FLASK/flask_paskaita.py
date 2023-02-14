from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     data = [{"Name": "Lina", "Surname": "Datkunaite"},{"Name": "Darius", "Surname": "Sagatauskas"}]
#     return  render_template('index.html', data=data)
# if __name__=='__main__':
#     app.run(host = '127.0.0.1', port=8000, debug=True)

# heroku.com galima padeployinti savo app
# https://127.0.0.1.0000   - musu local host (be domeno pvz www.delfi.lt jau yra domeno vardas)


@app.route('/') # kelias i adresa
def index():
    return  render_template('index.html')


@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/straipsniai')
def straipsniai():
    return  render_template("straipsniai.html")


if __name__=='__main__':
    app.run(host = '127.0.0.1', port=8000, debug=True)

