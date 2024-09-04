from flask import Blueprint, render_template, request, send_file, jsonify, url_for
from io import BytesIO

from app.elevenlabs_client import generate_speech

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        audio_data = generate_speech(text)
        audio_stream = BytesIO(audio_data)
        audio_stream.seek(0)
        return send_file(audio_stream, mimetype='audio/mpeg', as_attachment=False, download_name='output.mp3')

    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    audio_data = generate_speech(text)
    audio_stream = BytesIO(audio_data)
    audio_stream.seek(0)
    return send_file(audio_stream, mimetype='audio/mpeg', as_attachment=False)
