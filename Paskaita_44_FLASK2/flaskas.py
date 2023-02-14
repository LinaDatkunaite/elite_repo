from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/articles')
def articles():
    """TIPO ISSITRAUKEM IS DB"""
    data = [
        {
            'id': 1,
            'date': '2020 01 01',
            'author': 'Author 1',
            'title': 'About something',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                    'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero '
                    'undead survivor dictum mauris.',
            'status': 'published'
        },
        {
            'id': 2,
            'date': '2020 02 01',
            'author': 'Author 2',
            'title': 'About zombies',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                       'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger '
                       'omero undead survivor dictum mauris.',
            'status': 'unpublished'
        },
        {
            'id': 3,
            'date': '2020 03 01',
            'author': 'Author 3',
            'title': 'Braiiins!',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                       'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger '
                       'omero undead survivor dictum mauris.',
            'status': 'published'
        }
    ]
    return render_template("articles.html", data=data)


@app.route('/<int:id>')
def article(id):  # <-- i cia ateina kintamasis title is HTML
    data = [
        {
            'id': 1,
            'date': '2020 01 01',
            'author': 'Author 1',
            'title': 'About something',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                    'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero '
                    'undead survivor dictum mauris.',
            'status': 'published'
        },
        {
            'id': 2,
            'date': '2020 02 01',
            'author': 'Author 2',
            'title': 'About zombies',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                    'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger '
                    'omero undead survivor dictum mauris.',
            'status': 'unpublished'
        },
        {
            'id': 3,
            'date': '2020 03 01',
            'author': 'Author 3',
            'title': 'Braiiins!',
            'text': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering '
                    'animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger '
                    'omero undead survivor dictum mauris.',
            'status': 'published'
        }
    ]
    return render_template('article.html', id=id, data=data)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
