import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from config import Config
from models import db, EmployeeData
from preprocessing import DataPreprocessor
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

ALLOWED_EXTENSIONS = {'csv'}

# Initialize processed_data
processed_data = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global processed_data  # Declare global variable to hold processed data
    
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure the upload directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            file.save(filepath)

            try:
                # Preprocess the CSV file
                preprocessor = DataPreprocessor(filepath)
                records = preprocessor.preprocess()

                # Store preprocessed data in the database
                db.session.bulk_save_objects([EmployeeData(data=record) for record in records])
                db.session.commit()
                flash('File successfully uploaded and data processed.', 'success')

                # Save the processed data for visualization
                processed_data = pd.DataFrame(records).to_dict(orient='records')
                
            except Exception as e:
                db.session.rollback()
                flash(f'Error processing file: {e}', 'danger')
            finally:
                os.remove(filepath)  # Remove the uploaded CSV file from the folder

            return redirect(url_for('upload_file'))

    return render_template('upload.html', data=processed_data)

@app.route('/data')
def data():
    return jsonify(processed_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database tables are created
    app.run(debug=True)
