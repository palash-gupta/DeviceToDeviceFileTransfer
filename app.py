import os
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

app.secret_key = "lol"

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own

@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        flash('File(s) successfully uploaded')
        return redirect('/')


if __name__ == "__main__":
    app.run()