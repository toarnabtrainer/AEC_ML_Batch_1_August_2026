import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# creating a function for prediction
def win_loss_prediction(input_data):
    # changing and formatting the input
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction == "loss"):
        return "Prediction is LOSS..."
    else:
        return "Prediction is WIN..."
    
def main():
    # giving a title
    st.title("Win-Loss Prediction Web App...")
    # getting the inputs from the user
    # input_data = [0.4, 0.6]    # loss
    # input_data = [0.3, 0.6]    # win
    var1 = st.text_input("Enter a value for variable-1:")
    var2 = st.text_input("Enter a value for variable-2:")
    
    # code for prediction
    prediction = ""
    # creating a command button for prediction
    if (st.button("Predict Result")):
        prediction = win_loss_prediction([float(var1), float(var2)])
        st.success(prediction)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    