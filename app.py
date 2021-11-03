import flask
from flask import Flask, render_template, request, redirect, json
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['GET', 'POST'])
def index():
    url=request.form['x_values']
    try:
        youtube= YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        return render_template('thanks.html')

    except:
        return render_template('error.html')
    
@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('index.html')

@app.route('/playVideo')
def play():
    return render_template('video.html')
if __name__ == "__main__":
    app.run(debug=True)