from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from fastai.vision.all import *
import pathlib

#Labeling function required for load_learner to work
def getLabel(fileName):#this function should be the same with the label function you used in trainer
  return fileName.split('-')[0]

#pathlib.PosixPath = pathlib.WindowsPath
current_directory = pathlib.WindowsPath(__file__).resolve().parent
thepath = current_directory / 'export.pkl'

#fixes 'NotImplementedError'
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

learn = load_learner(thepath) #Import Model

pathlib.PosixPath = temp

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    img = PILImage.create(request.files['file'])
    label,_,probs = learn.predict(img)
    return f'{label} ({torch.max(probs).item()*100:.0f}%)'

if __name__=='__main__':
    #remove '#' and second app.run to run on local server
    #app.run(host="0.0.0.0", port=5000)
    app.run(debug = true) #'debug = true' to run webpage while editing



