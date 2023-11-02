from flask import Flask,render_template,url_for,request
import pickle
import numpy as np
import joblib
import pandas as pd
app=Flask(__name__)

#model_path = 'C:/Users/gts/phishing URL detection A real case scenario through ligin URLs/M2/Preprocessed dataset/phishing.pkl'
model_path=r"C:\Users\91950\major project\pickel\phishing.pkl"

model = joblib.load(
    open(model_path,'rb'))
print("model read")
@app.route('/')

def home():
    return render_template('ui.html')

@app.route('/result',methods=['POST'])
def predict():
    #print('test');
    text_URL = (request.form['text_URL'])
    print(text_URL)
    if text_URL.isalpha()==True or text_URL.isalnum()==True:
        return render_template('uinew.html',url=text_URL)
    

    prediction=model.predict([text_URL])
    #prediction = model.predict(['zimbio.com/Coco/articles/hgVpGi5atEj/Rapper+Ice+T+buxom+wife+Coco+reveals+breast'])#,'service.confirm.paypal.cmd.cgi-bin.2466sd4f3e6... '])
    print(prediction)
   
    return render_template('ui2.html',prediction=prediction,url=text_URL)
   
if __name__=='__main__':
    app.run(debug=True)
    
                       
    
    














