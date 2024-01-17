import joblib 
import os    
import streamlit as st 

import os

script_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_directory, 'house_predictor.pkl')
model = joblib.load(open(model_path, 'rb'))

# model = joblib.load(open('C:/Users/user/Desktop/Phase_IV/dsc-phase4-project/Choosing a Dataset/time-series/house_predictor.pkl', 'rb'))

def main():   
    
    st.title("House Predictor".upper())
    # st.markdown(f'<h1 style="color:#ff0000;">{title}</h1>', unsafe_allow_html=True)
    
    # st.image('house.jpg', use_column_width=True) 
    
    info = ''
    
    with st.expander("Check predicted value of houses"):
        text_image = st.date_input("Input the date")
        text_message = st.date_input("Input forecast time")
        
        if st.button("Predict"):
            info = model.predict([[text_image, text_message]])
            predicted_value = info.iloc[0]['y'] 
            st.success(f"The predicted value of the house is {predicted_value}")
            
            
if __name__ == '__main__':
    main() 
        
        