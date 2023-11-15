from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename #보안파일 가져오기 보안상 이유로 사용자에게 항목을 올바르게 업로드하도록 요청
from main_preprocessing import getPrediction
import os

UPLOAD_FOLDER = 'static/images/'

app = Flask(__name__, static_folder='static')

app.secret_key = 'secret key'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            label = getPrediction(filename)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')

if __name__ == '__main__':
    app.run()
