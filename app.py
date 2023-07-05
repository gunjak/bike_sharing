from src.pipeline.predict import CustomData, PredictPipeline
import streamlit as st


season={'winter':0,
        'summer':1,
        'spring':2,
        'fall':3}
month={'jan':1,'feb':2,'mar':3,
    'apr':4,'may':5,'jun':6,'july':7,
                            'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
day={'yes':1,'no':0}
weather={'clear':1,'cloudy':2,'light_snow':3,'heavy rain':4}


style = """<div style='background-color:pink; padding:12px'>
              <h1 style='color:black'>Bike Sharing Prediction App</h1>
       </div>"""
st.markdown(style, unsafe_allow_html=True)

data = CustomData(
            season = season[st.selectbox('season',('winter','summer','spring','fall'))],
            mnth = month[st.selectbox('month',('jan','feb','mar',
                            'apr','may','jun','july',
                            'aug','sep','oct','nov','dec'))],
            holiday= day[st.selectbox('Is there holiday',('yes','no'))],
            weekday= day[st.selectbox('weekday',('yes','no'))],
            workingday= day[st.selectbox('workingday',('yes','no'))],
            weathersit= weather[st.selectbox('weather',('clear','cloudy','light_snow','heavy rain'))],
            temp= st.number_input('temperature'),
            atemp= st.number_input('feeling temperature'),
            hum = st.number_input('humidity'),
            windspeed=st.number_input('windspeed')
        )


button = st.button('Predict')
if button:
    pred_df = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(pred_df)
    results = round(pred[0])
    st.success(f'total rental bikes including both casual and registered {results}')
    
    