import flask
from flask import Flask, render_template, request, redirect, json
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['GET', 'POST'])
def index():
    url=request.form['x_values']
    path = request.form['path']
    try:
        youtube= YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(path)
        return render_template('thanks.html')
    except Exception as e:
        f = str(e)
        return f
    
@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('index.html')

@app.route('/playVideo')
def play():
    return render_template('video.html')
if __name__ == "__main__":
    app.run(debug=True)