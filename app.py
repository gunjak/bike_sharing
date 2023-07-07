from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from src.pipeline.predict import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            season=int(request.form.get('season')),
            mnth=int(request.form.get('mnth')),
            holiday=int(request.form.get('holiday')),
            weekday=int(request.form.get('weekday')),
            workingday=int(request.form.get('workingday')),
            weathersit=int(request.form.get('weathersit')),
            temp=float(request.form.get('temp')),
            atemp=float(request.form.get('atemp')),
            hum=float(request.form.get('hum')),
            windspeed=float(request.form.get('windspeed')))
        
        pred_df=data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('index.html',results=results[0])
    
    

if __name__=="__main__":      
    app.run(host="0.0.0.0",port=8080)   