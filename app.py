# import warnings
# warnings.filterwarnings('ignore')

from flask import Flask, render_template, abort,flash,\
     Response, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
# import pickle
import numpy as np
# import tensorflow as tf
# from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
from utils import *
# import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['UPLOAD_FOLDER'] = os.path.join('static','uploads')
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.JPEG', '.jfif']
#upload model
model = load_model(model_path)
# logger = logging.getLogger()
# logger. propogate = True

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload Image")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if request.method=='POST':
        if form.validate_on_submit():
            # First grab the file
            file = form.file.data 
            filename = secure_filename(file.filename)
            abs_path_to_dir = os.path.abspath(os.path.dirname(__file__))
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
            
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    flash('Wrong File Format! Please Upload .jpg, .png, .jpeg, .jfif')
                    
                else:
                    flash('Image successfully uploaded!')
                    path = os.path.join(
                        abs_path_to_dir,
                        app.config['UPLOAD_FOLDER'],
                        filename)
                    file.save(path) # Then save the file
                    prediction = predict(path)
                    return render_template('predict.html', filename=filename, prediction=prediction)
                # return predict(path)
        # flash('problem with upload!')
    return render_template('home.html', form=form)

def predict(path):
    # if request.method == 'POST':
    try:
        file = image.load_img(path, target_size = (256,256))
        #normalize
        x=image.img_to_array(file)/255
        #add a batch dim
        x=np.expand_dims(x,axis=0)
        # x=preprocess_input(x)
        pred = model.predict(x)
        pred = np.argmax(pred, axis=1)
        # logger.log(pred)
        return return_string(pred)
    except Exception as e:
        # logger.error(e)
        print(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)