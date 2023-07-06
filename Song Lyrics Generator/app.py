from flask import Flask, render_template, request
from lyrics import scrapeLyricText
from markov import MarkovLyriscs

app = Flask(__name__)

def generateArtistLyrics(name):
    songs = scrapeLyricText(name)
    m = MarkovLyriscs()

    for song in songs:
        m.populateMarkovChain(song) # type: ignore
    lyrics = m.generateLyrics()
    return lyrics.split("NEWLINE")

@app.route('/', methods=['GET', 'POST'])
def lyricsGenerator():
    lyrics = []
    if request.method == "POST":
        artist = request.form['search']
        lyrics = generateArtistLyrics(artist)
    return render_template('home.html', lyrics=lyrics)

if __name__ == '__main__':
    app.run(debug=True)