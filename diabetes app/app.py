from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
from sklearn import preprocessing
app = Flask('__name__')
model=pickle.load(open('MERISkill.sav','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict', methods= ['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = model.predict(data)
        return render_template('predict.html', prediction=my_prediction)
  
    

    

if(__name__=='__main__'):
    app.run(debug=True)
