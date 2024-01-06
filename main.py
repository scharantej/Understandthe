 
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE genre='Action' ORDER BY rating DESC")
    movies = c.fetchall()
    conn.close()
    return render_template('index.html', movies=movies)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
    movie = c.fetchone()
    conn.close()
    return render_template('movie_details.html', movie=movie)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


**Validation and Corrections:**

After generating the Flask code, we need to validate the code to ensure that proper references to all the variables are made in the HTML files. In this case, we need to make sure that the `movies` variable in the `index.html` file and the `movie` variable in the `movie_details.html` file are correctly referenced.

In the `index.html` file, we need to replace the line:

html
{% for movie in movies %}


with:

html
{% for movie in movies.fetchall() %}


In the `movie_details.html` file, we need to replace the line:

html
{% for movie in movie %}


with:

html
{% for movie in movie.fetchall() %}


These changes ensure that the HTML files are correctly referencing the variables from the Flask code.

Once these corrections are made, the Flask application should work as expected, displaying a list of the best action movies on the homepage, detailed information about each movie on the movie details page, and contact information on the contact page.