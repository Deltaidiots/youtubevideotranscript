from flask import Blueprint, request, render_template, send_from_directory
from .utils import process_transcript
import os

main = Blueprint('main', __name__)

@main.route('/')
def upload_file():
    return render_template('upload.html')

@main.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            lines = file.read().decode('utf-8').split('\n')
            processed_transcript = process_transcript(lines)
            with open("output.txt", "w") as f:
                f.write(processed_transcript)
            return render_template('result.html', transcript=processed_transcript)
    return "No file uploaded."

@main.route('/download')
def download():
    return send_from_directory(os.getcwd(), "output.txt", as_attachment=True)
